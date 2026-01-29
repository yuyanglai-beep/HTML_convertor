"""
Word 文件處理核心模組
負責處理 Word 文件的內容控制項移除、段落轉換、表格轉換等功能
"""

from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from html import escape
import re


def remove_content_controls(doc):
    """
    移除 Word 文件中的內容控制項(表單欄位),轉換為一般文字
    
    Args:
        doc: python-docx Document 物件
    """
    sdt_nodes = list(doc.element.body.xpath('.//*[local-name()="sdt"]'))
    for sdt in sdt_nodes:
        parent = sdt.getparent()
        if parent is None:
            continue
        sdt_content = sdt.xpath('./*[local-name()="sdtContent"]')
        if sdt_content:
            sdt_content = sdt_content[0]
            insert_at = parent.index(sdt)
            for child in list(sdt_content):
                parent.insert(insert_at, child)
                insert_at += 1
            parent.remove(sdt)
        else:
            texts = sdt.xpath('.//*[local-name()="t"]')
            combined = ''.join(t.text or '' for t in texts)
            if combined.strip():
                run = OxmlElement(qn('w:r'))
                t = OxmlElement(qn('w:t'))
                t.text = combined
                run.append(t)
                parent.insert(parent.index(sdt), run)
            parent.remove(sdt)


def paragraph_to_html_with_links(para):
    """
    將 Word 段落轉換為 HTML,保留超連結
    
    Args:
        para: python-docx Paragraph 物件
        
    Returns:
        str: HTML 格式的段落內容
    """
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    runs_html = []
    for child in para._element:
        tag = child.tag.split('}')[-1]
        if tag == 'hyperlink':
            rel_id = child.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
            href = para.part.rels[rel_id].target_ref if rel_id and rel_id in para.part.rels else None
            link_text = ''.join(t.text or '' for t in child.findall('.//w:t', ns))
            if href:
                runs_html.append(f'<a href="{escape(href)}" target="_blank">{escape(link_text)}</a>')
            else:
                runs_html.append(escape(link_text))
        else:
            text = ''.join(t.text or '' for t in child.findall('.//w:t', ns))
            if text:
                runs_html.append(escape(text))
    if not runs_html:
        runs_html.append(escape(para.text or ''))
    return ''.join(runs_html)


def table_to_html(table):
    """
    將 Word 表格轉換為 HTML 表格
    
    Args:
        table: python-docx Table 物件
        
    Returns:
        str: HTML 格式的表格
    """
    html = ['<table style="border-collapse:collapse; table-layout:auto; border:1px solid #ccc; margin-left:0; margin-right:auto;">']
    for r_index, row in enumerate(table.rows):
        html.append('<tr>')
        for cell in row.cells:
            cell_content = []
            for para in cell.paragraphs:
                cell_content.append(paragraph_to_html_with_links(para))
            cell_html = "<br>".join(cell_content)
            if r_index == 0:
                cell_html = f"<strong>{cell_html}</strong>"
            html.append(f'<td style="border:1px solid #ccc; padding:6px; vertical-align:top;">{cell_html}</td>')
        html.append('</tr>')
    html.append('</table>')
    return ''.join(html)


def is_pure_url(text: str) -> bool:
    """
    判斷段落是否為單獨只有 URL
    
    Args:
        text: 要檢查的文字
        
    Returns:
        bool: 是否為純 URL
    """
    if not text:
        return False
    text = text.strip()
    return bool(re.fullmatch(r"https?://\S+", text))


def extract_embed_url(text: str):
    """
    從文字中抓出支援平台的網址 (IG / Threads / FB / YouTube)
    
    Args:
        text: 要搜尋的文字
        
    Returns:
        str or None: 找到的 URL,若無則返回 None
    """
    patterns = [
        r"https?://(?:www\.)?instagram\.com/[^\s]+",
        r"https?://(?:www\.)?threads\.net/[^\s]+",
        r"https?://(?:www\.)?facebook\.com/[^\s]+",
        r"https?://(?:www\.)?youtu\.be/[^\s]+",
        r"https?://(?:www\.)?youtube\.com/[^\s]+",
    ]
    for p in patterns:
        m = re.search(p, text)
        if m:
            return m.group(0)
    return None


def convert_url_to_iframe(url: str):
    """
    將 URL 轉換為嵌入式 iframe (依平台和類型自動調整高度)
    
    Args:
        url: 要轉換的 URL
        
    Returns:
        str or None: iframe HTML 程式碼,若不支援則返回 None
    """
    # Instagram 判斷 (/p/ = 圖文、/reel/ = 短影音、/tv/ = IGTV)
    if "instagram.com" in url:
        clean = url.split("?")[0].rstrip("/")
        
        if "/reel/" in clean:
            height = 800   # Reels
        elif "/tv/" in clean:
            height = 800   # IGTV
        else:
            height = 770   # 一般貼文(單圖/輪播)
        
        embed_url = clean + "/embed"
        
        return f'''
<p>
  <iframe
      src="{embed_url}"
      scrolling="no"
      style="
          width:100%;
          max-width:480px;
          height:{height}px;
          border:0;
          border-radius:14px;
          display:block;
          margin:0;
      ">
  </iframe>
</p>
'''
    
    # Threads 判斷 (文字/圖片/影片)
    if "threads.net" in url or "threads.com" in url:
        url = url.replace("threads.com", "threads.net")
        clean = url.split("?")[0].rstrip("/")
        embed_url = clean + "/embed"
        
        lower = url.lower()
        if "photo" in lower or "image" in lower:
            height = 580  # 圖片貼文
        elif "video" in lower or "reel" in lower:
            height = 650  # 影片貼文
        else:
            height = 480  # 文字貼文
        
        return f'''
<p>
  <iframe
      src="{embed_url}"
      scrolling="no"
      style="
          width:100%;
          max-width:480px;
          height:{height}px;
          border:0;
          border-radius:14px;
          display:block;
          margin:0;
      ">
  </iframe>
</p>
'''
    
    # YouTube (固定 16:9)
    if "youtube.com" in url or "youtu.be" in url:
        if "youtu.be" in url:
            vid = url.split("/")[-1]
        else:
            m = re.search(r"v=([^&]+)", url)
            vid = m.group(1) if m else ""
        
        return f'''
<p>
  <iframe
      src="https://www.youtube.com/embed/{vid}"
      style="
          width:100%;
          max-width:480px;
          height:270px;
          border:0;
          border-radius:14px;
          display:block;
          margin:0;
      "
      allowfullscreen>
  </iframe>
</p>
'''
    
    # Facebook (判斷:影片 or 貼文)
    if "facebook.com" in url:
        lower = url.lower()
        
        if "videos" in lower or "video" in lower or "watch" in lower:
            height = 900
        else:
            height = 600
        
        return f'''
<p>
  <iframe
      src="https://www.facebook.com/plugins/post.php?href={url}"
      scrolling="no"
      style="
          width:100%;
          max-width:480px;
          height:{height}px;
          border:0;
          border-radius:14px;
          display:block;
          margin:0;
      ">
  </iframe>
</p>
'''
    
    # 不支援的平台
    return None
