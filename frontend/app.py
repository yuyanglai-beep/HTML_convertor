"""
Word 轉 HTML 工具前端應用 (Gradio)
透過呼叫後端 API 提供 Word 轉 HTML 和圖片處理功能
"""

import gradio as gr
import requests
import tempfile
import os
import base64
from io import BytesIO
from PIL import Image
from config import BACKEND_URL

# ==========================================
# API 呼叫函數
# ==========================================

def call_convert_api(file_path, category):
    """呼叫後端 Word 轉換 API"""
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (os.path.basename(file_path), f, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')}
            data = {'category': category}
            response = requests.post(f"{BACKEND_URL}/api/convert-docx", files=files, data=data, timeout=60)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_detail = response.json().get('detail', '未知錯誤')
            raise Exception(f"API 錯誤: {error_detail}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"無法連接到後端服務: {str(e)}")


def call_image_api(file_path, width, height, quality):
    """呼叫後端圖片處理 API"""
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (os.path.basename(file_path), f)}
            data = {
                'width': int(width),
                'height': int(height),
                'quality': int(quality)
            }
            response = requests.post(f"{BACKEND_URL}/api/process-image", files=files, data=data, timeout=30)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_detail = response.json().get('detail', '未知錯誤')
            raise Exception(f"API 錯誤: {error_detail}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"無法連接到後端服務: {str(e)}")


# ==========================================
# Gradio Action 函數
# ==========================================

def convert_action(input_file, category_choice):
    """Word 轉換動作"""
    if input_file is None:
        gr.Info("⚠️ 請先上傳 Word 檔案")
        return None, None, None, None
    
    try:
        # 呼叫 API
        result = call_convert_api(input_file.name, category_choice)
        
        if result.get('success'):
            html_content = result.get('html', '')
            h1_title = result.get('title', '')
            
            # 儲存 HTML 到臨時檔案供下載
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w', encoding='utf-8')
            tmp.write(html_content)
            tmp.close()
            
            gr.Info("✅ 轉換成功!")
            return tmp.name, html_content, h1_title, html_content
        else:
            gr.Warning("❌ 轉換失敗")
            return None, None, None, None
    
    except Exception as e:
        gr.Warning(f"❌ 錯誤: {str(e)}")
        return None, None, None, None


def clear_action():
    """清除所有欄位"""
    gr.Info("🧹 已重置")
    return None, None, None, None, None, None


def process_image_action(img_file, width, height, quality):
    """圖片處理動作"""
    if img_file is None:
        gr.Info("⚠️ 請先上傳圖片")
        return None, None
    
    try:
        # 呼叫 API
        result = call_image_api(img_file.name, width, height, quality)
        
        if result.get('success'):
            # 解碼 base64 圖片
            image_data = result.get('image', '')
            if image_data.startswith('data:image'):
                image_data = image_data.split(',')[1]
            
            image_bytes = base64.b64decode(image_data)
            img = Image.open(BytesIO(image_bytes))
            
            info = result.get('info', '')
            
            return img, info
        else:
            gr.Warning("❌ 處理失敗")
            return None, ""
    
    except Exception as e:
        gr.Warning(f"❌ 錯誤: {str(e)}")
        return None, ""


def clear_image_action():
    """清除圖片欄位"""
    gr.Info("🧹 已重置圖片區")
    return None, 810, 540, 70, None, ""


# ==========================================
# UI 主題與樣式
# ==========================================

theme = gr.themes.Soft(
    primary_hue="blue",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Noto Sans TC"), "sans-serif"]
)

css = """
/* 整體深色背景 */
body, .gradio-container {
    background: radial-gradient(
        circle at top left,
        #1f2937 0,
        #020617 40%,
        #000 100%
    ) !important;
    color: #e5e7eb !important;
}

/* Panel / Box */
.gr-panel, .gr-box, .gr-group, .gr-form,
.gr-column > .container, .gr-row > .container {
    background: rgba(15, 23, 42, 0.92) !important;
    border-radius: 18px !important;
    border: 1px solid rgba(148, 163, 184, 0.35) !important;
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.65) !important;
    overflow: visible !important;
}

/* 區塊標題 */
.gr-box > .gr-markdown h3,
.gr-box > .gr-markdown h2 {
    color: #e5e7eb !important;
}

/* Label 玻璃效果 */
label[data-testid="block-label"],
.gr-file > label,
.label-wrap > label,
.form-label > label,
.gr-form > label {
    background: rgba(30, 41, 59, 0.38) !important;
    padding: 6px 14px !important;
    border-radius: 12px !important;
    color: #e5e7eb !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    letter-spacing: 0.02em;
    border: 1px solid rgba(148, 163, 184, 0.25) !important;
    backdrop-filter: blur(6px) !important;
    -webkit-backdrop-filter: blur(6px) !important;
    box-shadow: 0 4px 14px rgba(59,130,246,0.18) !important;
}
.gr-markdown h1 label,
.gr-markdown h2 label,
.gr-markdown h3 label {
    background: none !important;
    box-shadow: none !important;
    border: none !important;
}
span[data-testid="block-info"] {
    background: rgba(30, 41, 59, 0.42) !important;
    color: #e5e7eb !important;
    padding: 6px 14px !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    letter-spacing: .02em;
    border: 1px solid rgba(148, 163, 184, .25) !important;
    backdrop-filter: blur(6px) !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.20) !important;
}
.wrap.svelte-1hfxprf.container {
    background: rgba(15, 23, 42, 0.25) !important;
    border: 1px solid rgba(71, 85, 105, .35) !important;
    border-radius: 12px !important;
    padding: 6px 6px !important;
    backdrop-filter: blur(4px) !important;
}

/* 移除子物件捲軸 */
.gradio-container * {
    scrollbar-width: none !important;
}
.gradio-container *::-webkit-scrollbar {
    width: 0 !important;
    height: 0 !important;
}

/* Preview 區 */
#preview-box, #code-box .cm-scroller, #img-preview-box {
    height: 600px !important;
    max-height: 600px !important;
    overflow-y: auto !important;
    border-radius: 14px !important;
    border: 1px solid rgba(55, 65, 81, 0.95) !important;
    background: radial-gradient(
        circle at top left,
        #0f172a 0,
        #020617 55%,
        #020617 100%
    ) !important;
    padding: 16px !important;
    color: #e5e7eb !important;
    font-size: 14px;
}
#img-preview-box img {
    max-width: 100%;
    height: auto;
    border-radius: 12px;
}

/* 表單欄位 */
.gradio-container .gr-input,
.gradio-container .gr-select,
.gradio-container .gr-file {
    background-color: rgba(15, 23, 42, 0.95) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(71, 85, 105, 0.9) !important;
    color: #e5e7eb !important;
}

/* 按鈕樣式 */
#convert-btn, #clear-btn, #img-convert-btn, #img-clear-btn {
    position: relative;
    overflow: hidden;
    border-radius: 999px !important;
    padding: 0.6rem 1.4rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.04em;
    transition: all 0.22s ease-out;
}
#convert-btn, #img-convert-btn {
    border: 1px solid rgba(96, 165, 250, 0.7) !important;
    color: #e5e7eb !important;
    background: radial-gradient(
        circle at 0% 0%,
        rgba(56, 189, 248, 0.85) 0,
        rgba(37, 99, 235, 0.95) 40%,
        rgba(15, 23, 42, 1) 100%
    ) !important;
    box-shadow:
        0 0 0 1px rgba(15, 23, 42, 0.9),
        0 12px 30px rgba(37, 99, 235, 0.55);
}
#convert-btn:hover, #img-convert-btn:hover {
    box-shadow:
        0 0 0 1px rgba(191, 219, 254, 0.9),
        0 18px 45px rgba(56, 189, 248, 0.75);
    transform: translateY(-1px) scale(1.02);
}
#clear-btn, #img-clear-btn {
    border: 1px solid rgba(148, 163, 184, 0.7) !important;
    color: #e5e7eb !important;
    background: linear-gradient(
        135deg,
        rgba(31, 41, 55, 0.95),
        rgba(15, 23, 42, 1)
    ) !important;
    box-shadow:
        0 0 0 1px rgba(15, 23, 42, 1),
        0 10px 26px rgba(15, 23, 42, 0.9);
}
#clear-btn:hover, #img-clear-btn:hover {
    border-color: rgba(209, 213, 219, 0.95) !important;
    transform: translateY(-1px);
}
#convert-btn::before,
#clear-btn::before,
#img-convert-btn::before,
#img-clear-btn::before {
    content: "";
    position: absolute;
    top: 0;
    left: -120%;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        120deg,
        transparent 0%,
        rgba(255, 255, 255, 0.25) 40%,
        rgba(255, 255, 255, 0.75) 50%,
        rgba(255, 255, 255, 0.25) 60%,
        transparent 100%
    );
    opacity: 0;
}
#convert-btn:hover::before,
#clear-btn:hover::before,
#img-convert-btn:hover::before,
#img-clear-btn:hover::before {
    opacity: 1;
    animation: shimmer-slide 0.9s ease-out forwards;
}
@keyframes shimmer-slide {
    0% { transform: translateX(0); left: -120%; }
    100% { transform: translateX(120%); left: 120%; }
}
#left-panel { padding: 18px 20px !important; }
#right-panel { padding: 18px 22px !important; }

#left-panel-img { padding: 18px 20px !important; }
#right-panel-img { padding: 18px 22px !important; }

/* 移除圖片工具分享按鈕 */
#img-preview-box .svelte-1ipelgc:nth-of-type(3),
#img-preview-box button[aria-label="Share"] {
    display: none !important;
}
#img-preview-box .svelte-1ipelgc {
    opacity: 1 !important;
}
#img-preview-box img {
    image-rendering: auto;
}
"""

# ==========================================
# Gradio 介面
# ==========================================

with gr.Blocks(title="Word 轉 HTML 工具") as demo:

    with gr.Row():
        with gr.Column():
            gr.Markdown("## 📝 Word 轉 HTML 工具")

            with gr.Accordion("📘 操作說明(點擊展開)", open=False):
                gr.HTML("""
                <div style="line-height:1.7; font-size:16px;">

                  <h2 style="margin-bottom:10px;">🛠️ 這個工具能幫你做什麼?</h2>

                  <ul style="margin-left:18px;">
                    <li><strong>自動把 Word 原稿轉成官網可用的 HTML</strong>(標題階層、段落、空行全部重整)</li>
                    <li><strong>自動把獨立一行的 URL 轉成嵌入卡片</strong>(IG / Threads / FB / YouTube)</li>
                    <li><strong>支援智慧判斷</strong>(例如 IG Reel、圖片帖、FB 影片等會自動調整嵌入高度)</li>
                    <li><strong>Word 表格 → 完整 HTML 表格</strong>(邊框、粗體、自動排版)</li>
                    <li><strong>圖片壓縮＋調整尺寸</strong>(第二個分頁可一次處理)</li>
                    <li><strong>自動加上 Footer CTA</strong>(依分類套用不同的 Footer 樣式)</li>
                  </ul>

                  <br>

                  <h2 style="margin-bottom:10px;">📌 開始前一定要確認的 3 件事</h2>
                  <ul style="margin-left:18px; list-style-type: square;">
                    <li><strong>標題階層要正確:</strong>H1=主標、H2=大標、H3=小標(H1 會自動抽出,不顯示在文章內)</li>
                    <li><strong>網址要獨立成一行:</strong>整行只有 URL 才會轉成卡片</li>
                    <li><strong>空行不用手動調整:</strong>系統會自動調整漂亮排版</li>
                  </ul>

                  <br>

                  <h2 style="margin-bottom:10px;">🚀 轉檔步驟</h2>
                  <ol style="margin-left:18px;">
                    <li>上傳 <code>.docx</code> 原稿</li>
                    <li>選擇文章分類(會自動套用對應 Footer)</li>
                    <li>按下「開始轉換」</li>
                    <li>右側可預覽、可複製,也能直接下載 HTML 檔</li>
                  </ol>

                  <br>

                  <h2 style="margin-bottom:6px;">📄 範例原稿下載(Demo)</h2>
                  <p>以下是「建議格式」的示範檔,你可以下載照著排,轉檔最穩定:</p>

                  <a href="https://docs.google.com/document/d/1lUKgxM--8VeTYHpvX7hdlb19toZ2VYh8/export?format=docx"
                     download
                     style="
                        display:inline-block;
                        padding:10px 20px;
                        margin-top:8px;
                        border-radius:12px;
                        background:linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
                        color:white;
                        font-weight:600;
                        text-decoration:none;
                        letter-spacing:0.03em;
                        box-shadow:0 4px 14px rgba(37, 99, 235, 0.35);
                     ">
                     📎 點我下載 converter_demo.docx(範例原稿)
                  </a>

                  <br><br>

                </div>
                """)

    with gr.Tabs():
        # 文章轉檔
        with gr.TabItem("📝 文章轉檔"):
            with gr.Row(equal_height=False):
                with gr.Column(scale=1, elem_id="left-panel"):
                    gr.Markdown("### 🔧 設定與動作")

                    file_input = gr.File(
                        label="📂 上傳 Word 檔(.docx)",
                        file_types=[".docx"],
                        file_count="single"
                    )

                    category_choice = gr.Dropdown(
                        choices=[
                            "🔵 數據分析解方",
                            "🔷 產業口碑數據",
                            "🟦 消費者洞察",
                            "🩷 網紅行銷策略",
                            "🟡 社群粉絲團健檢",
                            "🟣 Threads 行銷服務"
                        ],
                        label="#️⃣文章分類(決定 Footer)",
                        value="🔵 數據分析解方",
                        interactive=True
                    )

                    with gr.Row():
                        convert_btn = gr.Button("✨ 開始轉換", variant="primary", elem_id="convert-btn")
                        clear_btn = gr.Button("🧹 重置", elem_id="clear-btn")

                    download_output = gr.File(visible=False)

                with gr.Column(scale=3, elem_id="right-panel"):
                    gr.Markdown("### 📄 轉換結果")

                    h1_output = gr.Textbox(
                        label="🔖主標題(H1)",
                        interactive=False,
                        # show_copy_button=True (Gradio 4+ deprecated for Textbox in some versions, default is usually ok or use copy component)
                    )

                    with gr.Tabs():
                        with gr.TabItem("🌐 HTML 預覽"):
                            html_preview = gr.HTML(label="HTML Preview", elem_id="preview-box")
                        with gr.TabItem("💻 HTML 原始碼"):
                            code_output = gr.Code(
                                language="html",
                                label="HTML Code",
                                interactive=False,
                                elem_id="code-box"
                            )

            convert_btn.click(
                fn=convert_action,
                inputs=[file_input, category_choice],
                outputs=[download_output, html_preview, h1_output, code_output]
            )

            clear_btn.click(
                fn=clear_action,
                inputs=None,
                outputs=[file_input, download_output, category_choice, html_preview, h1_output, code_output]
            )

        # 圖片工具
        with gr.TabItem("🖼️ 圖片壓縮調整大小"):
            with gr.Row(equal_height=False):
                with gr.Column(scale=1, elem_id="left-panel-img"):
                    gr.Markdown("### 🔧 圖片設定與動作")

                    img_input = gr.File(
                        label="📎 上傳圖片(jpg / png / webp)",
                        file_types=[".jpg", ".jpeg", ".png", ".webp"],
                        file_count="single"
                    )

                    width_in = gr.Number(label="寬度(px)", value=810, precision=0)
                    height_in = gr.Number(label="高度(px)", value=540, precision=0)

                    quality_in = gr.Slider(
                        minimum=30, maximum=95, value=70, step=1,
                        label="壓縮品質(%)"
                    )

                    with gr.Row():
                        img_convert_btn = gr.Button("✨ 開始處理", variant="primary", elem_id="img-convert-btn")
                        img_clear_btn = gr.Button("🧹 重置", elem_id="img-clear-btn")

                with gr.Column(scale=3, elem_id="right-panel-img"):
                    gr.Markdown("### 👀 圖片預覽")
                    img_preview = gr.Image(
                        label="Preview",
                        elem_id="img-preview-box",
                        format="jpeg"
                    )

                    img_info = gr.Markdown("")

            img_convert_btn.click(
                fn=process_image_action,
                inputs=[img_input, width_in, height_in, quality_in],
                outputs=[img_preview, img_info]
            )

            img_clear_btn.click(
                fn=clear_image_action,
                inputs=None,
                outputs=[img_input, width_in, height_in, quality_in, img_preview, img_info]
            )

if __name__ == "__main__":
    os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"
    print(f"🔗 連接到後端 API: {BACKEND_URL}")
    demo.launch(
        show_error=True, 
        ssr_mode=False,
        server_name="0.0.0.0",
        server_port=7860,
        theme=theme,
        css=css
    )
