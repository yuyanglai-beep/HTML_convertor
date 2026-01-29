# 📖 Word 轉 HTML 工具使用指南

## 🎯 工具簡介

這是一個專業的 Word 文件轉 HTML 工具,可以幫你:

- 將 Word 文件轉換為網頁 HTML 格式
- 自動嵌入社群媒體內容 (Instagram、Threads、Facebook、YouTube)
- 處理和壓縮圖片
- 自動生成文章目錄
- 依分類套用不同的 Footer 樣式

---

## 🚀 快速開始

### 步驟 1: 啟動工具

#### Windows 使用者

雙擊執行 `start.bat` 或在命令提示字元中執行:

```bash
cd c:\Users\yuyan\.gemini\antigravity\playground\photonic-filament
start.bat
```

#### Mac/Linux 使用者

在終端機中執行:

```bash
cd /path/to/photonic-filament
chmod +x start.sh
./start.sh
```

### 步驟 2: 開啟網頁介面

啟動後,會自動開啟兩個視窗:

- **後端服務** (Port 8000) - 處理轉換邏輯
- **前端介面** (Port 7860) - 使用者操作介面

在瀏覽器中訪問:

```
http://localhost:7860
```

---

## 📝 功能 1: Word 轉 HTML

### 使用步驟

1. **上傳 Word 檔案**
   - 點擊「上傳 Word 檔案」按鈕
   - 選擇你的 `.docx` 檔案
   - 支援包含圖片、表格、超連結的 Word 文件

2. **選擇文章分類**
   - 從下拉選單選擇分類
   - 不同分類會套用不同的 Footer CTA
   - 可用分類:
     - 🔵 數據分析解方
     - 🔷 產業口碑數據
     - 🟦 消費者洞察
     - 🩷 網紅行銷策略
     - 🟡 社群粉絲團健檢
     - 🟣 Threads 行銷服務

3. **點擊「開始轉換」**
   - 工具會自動處理你的文件
   - 轉換通常在 1-3 秒內完成

4. **查看結果**
   - **HTML 預覽**: 查看轉換後的網頁效果
   - **HTML 原始碼**: 查看完整的 HTML 程式碼
   - **主標題 (H1)**: 顯示文章的主標題

5. **下載 HTML**
   - 點擊「下載 HTML」按鈕
   - 檔案會以 `{主標題}.html` 命名
   - 可直接複製 HTML 原始碼使用

### 💡 Word 文件撰寫技巧

#### 標題設定

- **H1 (標題 1)**: 文章主標題 (只會顯示,不會出現在內容中)
- **H2 (標題 2)**: 主要章節標題
- **H3 (標題 3)**: 次要章節標題

工具會自動:

- 生成可點擊的文章目錄
- 在第一個 H2 前插入目錄
- 設定平滑捲動效果

#### 社群媒體嵌入

只需在 Word 中**單獨一行**貼上完整的 URL,工具會自動轉換為嵌入卡片:

**支援的平台:**

| 平台 | URL 範例 | 自動識別類型 |
|------|---------|-------------|
| Instagram | `https://www.instagram.com/p/ABC123/` | 圖文貼文 |
| Instagram | `https://www.instagram.com/reel/ABC123/` | Reels 短影音 |
| Threads | `https://www.threads.net/@user/post/ABC123` | 文字/圖片/影片 |
| Facebook | `https://www.facebook.com/user/posts/123` | 一般貼文 |
| Facebook | `https://www.facebook.com/watch/?v=123` | 影片貼文 |
| YouTube | `https://www.youtube.com/watch?v=ABC123` | 影片 |
| YouTube | `https://youtu.be/ABC123` | 短網址 |

**注意事項:**

- URL 必須**單獨一行**,不要有其他文字
- 會自動調整嵌入高度 (依內容類型)
- 嵌入卡片會自動置中顯示

#### 表格處理

Word 表格會自動轉換為 HTML 表格:

- 保留邊框和儲存格樣式
- 第一行自動加粗 (作為表頭)
- 自動調整欄寬

#### 超連結

Word 中的超連結會自動保留:

- 點擊後在新分頁開啟
- 保留原始連結文字

---

## 🖼️ 功能 2: 圖片處理

### 使用步驟

1. **切換到「圖片處理」分頁**
   - 點擊頁面上方的「圖片處理」標籤

2. **上傳圖片**
   - 支援格式: JPG、PNG、WebP
   - 可一次上傳一張圖片

3. **設定參數**
   - **寬度**: 預設 810px (可自訂)
   - **高度**: 預設 540px (可自訂)
   - **品質**: 預設 70% (範圍 30-95%)
     - 70%: 平衡品質和檔案大小 (推薦)
     - 85%: 高品質,檔案較大
     - 50%: 較小檔案,品質略降

4. **點擊「開始處理」**
   - 工具會自動調整尺寸和壓縮
   - 顯示處理後的圖片預覽
   - 顯示檔案大小資訊

5. **下載圖片**
   - 點擊「下載圖片」按鈕
   - 檔案會以 `processed_image.jpg` 命名

### 💡 圖片處理技巧

**常用尺寸建議:**

- **文章橫幅**: 810×540px (預設)
- **社群媒體**: 1080×1080px (正方形)
- **縮圖**: 400×300px

**品質設定建議:**

- **網頁使用**: 70% (平衡)
- **高品質展示**: 85%
- **快速載入**: 50-60%

---

## 🎨 進階功能

### 自動生成目錄 (TOC)

工具會自動:

1. 掃描所有 H2 和 H3 標題
2. 在第一個 H2 前插入目錄
3. 生成可點擊的錨點連結
4. 設定平滑捲動效果

**目錄樣式:**

- H2: 主要項目 (•)
- H3: 次要項目 (◦,縮排)

### Footer CTA 自動套用

依據選擇的分類,會自動在文章底部加上對應的 Footer:

- 包含精美的 CTA 卡片
- 自動套用品牌色彩和樣式
- 包含行動呼籲按鈕

### 智慧空行處理

工具會自動:

- 移除多餘的空行
- 在標題前後保留適當間距
- 在 iframe 嵌入前後保留空行
- 確保排版整齊美觀

---

## ❓ 常見問題

### Q1: 轉換失敗怎麼辦?

**可能原因:**

1. Word 檔案損壞
2. 檔案包含不支援的元素
3. 後端服務未啟動

**解決方法:**

1. 確認後端服務正在運行 (Port 8000)
2. 檢查 Word 檔案是否可正常開啟
3. 嘗試重新啟動工具

### Q2: 社群媒體 URL 沒有轉換為嵌入卡片?

**檢查清單:**

- [ ] URL 是否**單獨一行**
- [ ] URL 是否完整 (包含 https://)
- [ ] URL 是否為支援的平台
- [ ] URL 前後是否有其他文字

**正確範例:**

```
這是一段文字。

https://www.instagram.com/p/ABC123/

這是另一段文字。
```

**錯誤範例:**

```
請看這個連結 https://www.instagram.com/p/ABC123/ 很棒吧!
```

### Q3: 圖片處理後檔案太大?

**解決方法:**

1. 降低品質設定 (例如從 70% 降到 50%)
2. 縮小尺寸 (例如從 810px 降到 600px)
3. 使用 JPG 格式 (比 PNG 小)

### Q4: 如何修改 Footer 內容?

Footer 內容儲存在 `backend/templates/footers.py`:

1. 用文字編輯器開啟檔案
2. 找到對應的 `FOOTER_XXX` 變數
3. 修改 HTML 內容
4. 重新啟動後端服務

### Q5: 可以批次處理多個檔案嗎?

目前版本一次只能處理一個檔案。如需批次處理:

1. 使用 API 端點自行開發
2. 或逐一上傳處理

---

## 🔧 進階設定

### 修改後端 API URL

如果後端部署在其他位置,可修改 `frontend/config.py`:

```python
BACKEND_URL = "http://your-backend-url:8000"
```

或設定環境變數:

```bash
# Windows
set BACKEND_URL=http://your-backend-url:8000

# Mac/Linux
export BACKEND_URL=http://your-backend-url:8000
```

### 新增文章分類

1. 編輯 `backend/templates/footers.py`
2. 新增 Footer HTML:

   ```python
   FOOTER_NEW = """<div>你的 HTML</div>"""
   ```

3. 加入對應關係:

   ```python
   CATEGORY_TO_FOOTER_HTML = {
       "🆕 新分類": FOOTER_NEW,
       # ... 其他分類
   }
   ```

4. 編輯 `frontend/app.py`,在分類選單中加入新選項

---

## 📞 需要協助?

如遇到問題:

1. 查看終端機的錯誤訊息
2. 確認前後端服務都正常運行
3. 查看 [README.md](file:///c:/Users/yuyan/.gemini/antigravity/playground/photonic-filament/README.md) 的詳細說明
4. 提交 GitHub Issue

---

## 🎉 開始使用

現在你已經了解如何使用這個工具了!

**快速提醒:**

1. 執行 `start.bat` (Windows) 或 `start.sh` (Mac/Linux)
2. 訪問 <http://localhost:7860>
3. 上傳 Word 檔案
4. 選擇分類
5. 開始轉換!

祝你使用愉快! 🚀
