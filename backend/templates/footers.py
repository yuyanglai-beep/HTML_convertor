"""
Footer 模板定義
包含所有文章分類對應的 Footer HTML
"""

FOOTER_VOC = """<div class="cta-card-wrapper"><div class="cta-card footer-card"><p class="footer-text"><em><strong class="footer-strong">i-Buzz 行業資料庫</strong><span class="footer-normal"> 提供各產業完整的品牌、產品資訊與熱門話題內容。您只需告訴我們想了解的產業領域,無需設定繁複關鍵字,即可快速取得可靠的行業口碑洞察。如需更深入的數據應用與分析服務,歡迎填寫表單與我們聯繫。</span></em></p><p class="footer-btn-area"><a href="https://www.i-buzz.com.tw/user/contact/" target="_blank"><img src="/uploads/industry_img/1712050466.png" alt="CTA" width="200" height="65"></a></p></div></div><style>.cta-card-wrapper { display: flex; justify-content: center; margin: 40px 0; } .footer-card { max-width: 720px; background: linear-gradient(180deg, #f4e9dc 0%, #fffdf9 90%); padding: 38px 45px; border-radius: 18px; border: none; box-shadow: 0 10px 28px rgba(140, 110, 70, 0.18); } .footer-text { font-size: 16px; line-height: 1.85; margin-bottom: 28px; color: #5a371e; } .footer-normal { color: #5a371e; } .footer-strong { color: #7b4a21; font-weight: 700; } .footer-btn-area { text-align: center; }</style>"""

FOOTER_TREND = """<div class="cta-card-wrapper"><div class="cta-card footer-card"><p class="footer-text"><em><span class="footer-normal">i-Buzz為台灣首間網路口碑研究中心,累積超過16年的跨產業口碑分析經驗, 提供客戶 </span> <strong class="footer-strong">i-Buzz VOC+ 產業口碑數據庫、商業策略分析</strong> <span class="footer-normal"> 、消費者輪廓洞察及口碑行銷優化等全方位服務。 歡迎填寫表單,讓專業的團隊為您服務! </span> </em></p><p class="footer-btn-area"><a href="https://www.i-buzz.com.tw/user/contact/" target="_blank"><img alt="CTA" height="65" src="/uploads/industry_img/1712050466.png" width="200" /> </a></p></div></div><style type="text/css">.cta-card-wrapper { display: flex; justify-content: center; margin: 40px 0; } .footer-card { max-width: 720px; background: linear-gradient(180deg, #f4e9dc 0%, #fffdf9 90%); padding: 38px 45px; border-radius: 18px; border: none; box-shadow: 0 10px 28px rgba(140, 110, 70, 0.18); } .footer-text { font-size: 16px; color: #5a371e; line-height: 1.85; margin-bottom: 28px; } .footer-normal { color: #5a371e; } .footer-strong { color: #7b4a21; font-weight: 700; } .footer-btn-area { text-align: center; }</style>"""

FOOTER_AK = """
 <div class="cta-box">
<div class="cta-one">
<p><strong>⭐ <strong>「AsiaKOL 網紅專案式顧問服務」</strong></strong><strong background-color:="" noto="" sans="" style="font-size: 18px; color: rgb(44, 122, 123); font-family: " text-align:=""><strong>,</strong></strong><strong><strong>從網紅精準篩選、創意內容企劃到專案執行與監測,全程由專業團隊一手打造。</strong><br />
若您想了解更多服務內容,或希望由專人協助規劃合作,歡迎點擊下方: </strong></p>

<div class="cta-btn-wrap"><a class="cta-btn2" href="https://www.asiakol.com/page/view/service/project" target="_blank">服務介紹</a> <a class="cta-btn2" href="https://www.asiakol.com/page/view/contact-us" target="_blank">填寫需求單</a></div>
</div>
</div>

<p>&nbsp;</p>
<style type="text/css">.cta-box {
    border: 1.5px solid #c7d8d8;
    border-radius: 10px;
    padding: 50px 22px;
    max-width: 820px;
    margin: 40px auto;
    background: #f9fcfc;
  }
  .cta-one {
    text-align: center;
    color: #2c7a7b;
    font-family: "Noto Sans TC", sans-serif;
    line-height: 1.7;
  }
  .cta-btn-wrap {
    margin-top: 18px;
    display: flex;
    justify-content: center;
    gap: 14px;
    flex-wrap: wrap;
  }
  /* 增加權重並確保所有狀態都是白色 */
  a.cta-btn2, a.cta-btn2:visited {
    display: inline-block;
    padding: 10px 22px;
    background-color: #2c7a7b !important;
    color: #ffffff !important; /* 強制執行白色 */
    border-radius: 6px;
    text-decoration: none !important;
    font-size: 15px;
    font-weight: 600;
    transition: 0.25s;
  }
  a.cta-btn2:hover {
    background-color: #225f61 !important;
    color: #ffffff !important;
  }
</style>
"""

FOOTER_FF = """
<hr />
<p style="margin: 0px; padding: 0px;">
  <span id="docs-internal-guid-008b77ae-7fff-c582-a34d-ac1dfa7fefd7">
    <span style="font-weight: 700; font-family: Arial, sans-serif; font-size: 12pt; color: rgb(255, 255, 255); background-color: rgb(0, 0, 128);">FANS FEED 品牌頻道經營</span>
  </span>
</p>
<p style="margin: 14pt 0px; line-height: 1.2;">
  <span id="docs-internal-guid-008b77ae-7fff-c582-a34d-ac1dfa7fefd7">
    <span style="font-family: REM, sans-serif; font-size: 12pt; color: rgb(85, 85, 85);"> ⭐ </span>
    <span style="font-family: Arial, sans-serif; font-size: 12pt; color: rgb(85, 85, 85);"> </span>
    <span style="font-family: Arial, sans-serif; font-size: 12pt; color: rgb(0, 0, 128);">品牌小編努力發文,成效卻不見起色嗎?你需要經驗豐富的專業小編團隊,為你管理官方社群頻道,以數據分析及深度觀察達到內容精采度與宣傳成效&nbsp;►&nbsp;</span>
    <a href="https://fansfeed.com.tw/cultivateserve_p1_1" style="text-decoration-line: none; color: rgb(66, 174, 251);" target="_blank">
      <span style="font-weight: 700; font-family: Arial, sans-serif; font-size: 12pt; color: rgb(255, 255, 255); background-color: rgb(0, 128, 128); text-decoration-line: underline;">了解更多</span>
    </a>
  </span>
</p>
<p style="margin: 14pt 0px 0pt; line-height: 1.2;">
  <span style="font-size: 12pt; font-family: REM, sans-serif; color: rgb(85, 85, 85);"> ⭐ </span>
  <span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(85, 85, 85);"> </span>
  <span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(0, 0, 128);">填寫需求單,將有專業團隊為你服務&nbsp;►</span>
  <span style="color: rgb(255, 255, 255);"><span style="font-family: Arial, sans-serif;">&nbsp;</span></span>
  <span style="font-size: 12pt; font-family: Arial, sans-serif; font-weight: 700; background-color: rgb(0, 128, 128);">
    <span>
      <span>
        <a href="https://fansfeed.com.tw/index#CBArrow" style="text-decoration-line: none; color: rgb(66, 174, 251);" target="_blank">
          <span style="color: rgb(255, 255, 255);">立即填寫</span>
        </a>
      </span>
    </span>
  </span>
</p>
"""

FOOTER_THREADS = """<div class="cta-card-wrapper"><div class="cta-card"><p class="cta-title"><strong>Threads 爆發力強、紅利正旺!</strong></p><p class="cta-subtitle">在高流量、高競爭的環境裡,品牌只有一次被看見的機會。</p><p class="cta-desc">i-Buzz Threads 行銷服務,讓你的內容更有話題、更容易衝上熱度高點。</p><p class="cta-highlight"><span class="highlight-light">想讓品牌成為下一個爆紅案例?</span><span class="highlight-bold">和我們聊聊吧。</span></p><p class="cta-btn-area"><a href="https://www.i-buzz.com.tw/article/threadsmarketing#treads_sec_4" target="_blank"><img src="https://www.i-buzz.com.tw/uploads/industry_img/1712050466.png" alt="CTA" width="220" height="70"></a></p></div></div><style type="text/css">.cta-card-wrapper { display: flex; justify-content: center; margin: 40px 0; } .cta-card { max-width: 720px; background: linear-gradient(180deg, #f6f3ff 0%, #ffffff 85%); padding: 40px 45px; border-radius: 22px; box-shadow: 0 14px 36px rgba(80, 60, 140, 0.15); border: 1px solid #ece8ff; } .cta-title { font-size: 30px; font-weight: 800; color: #4f17b1; margin: 0 0 4px; line-height: 1.3; } .cta-subtitle { font-size: 18px; color: #4f17b1; margin: 0 0 28px; line-height: 1.45; } .cta-desc { font-size: 17px; color: #7c6af2; line-height: 1.75; margin-bottom: 22px; } .cta-highlight { font-size: 19px; line-height: 1.7; margin-bottom: 32px; } .highlight-light { color: #8e7dfa; } .highlight-bold { color: #4f17b1; font-weight: 700; } .cta-btn-area { text-align: center; margin-top: 10px; }</style>"""

# 分類對應表
CATEGORY_TO_FOOTER_HTML = {
    "🔵 數據分析解方": FOOTER_VOC,
    "🔷 產業口碑數據": FOOTER_TREND,
    "🟦 消費者洞察": FOOTER_VOC,
    "🩷 網紅行銷策略": FOOTER_AK,
    "🟡 社群粉絲團健檢": FOOTER_FF,
    "🟣 Threads 行銷服務": FOOTER_THREADS
}
