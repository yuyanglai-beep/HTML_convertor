# Word 轉 HTML 工具

> 專為 Word 文件轉換 HTML 設計的工具，支援一鍵轉換、圖片處理與自動套用 Footer
> 
> 📅 最後更新：2026-01-30

<div align="center">

![Word to HTML](https://img.shields.io/badge/Word-to--HTML-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi)
![Gradio](https://img.shields.io/badge/Gradio-4.16-orange?style=for-the-badge)

**專業的 Word 文件轉 HTML 工具,支援社群媒體嵌入和圖片處理**

[功能特色](#功能特色) • [快速開始](#快速開始) • [API 文件](#api-文件) • [部署指南](#部署指南)

</div>

---

## 📖 專案簡介

這是一個前後端分離的 Web 應用程式,專為內容編輯團隊設計,能夠:

- 🔄 **自動轉換** Word 文件為符合官網規範的 HTML
- 🎯 **智慧嵌入** Instagram、Threads、Facebook、YouTube 等社群媒體內容
- 📊 **表格處理** 完整保留 Word 表格格式和樣式
- 🖼️ **圖片優化** 批次調整圖片尺寸和壓縮品質
- 🎨 **自動排版** 智慧調整標題階層、段落間距和目錄生成

## ✨ 功能特色

### Word 轉 HTML

- ✅ 自動識別標題階層 (H1/H2/H3)
- ✅ 保留超連結和文字格式
- ✅ 自動生成文章目錄 (TOC)
- ✅ 平滑捲動錨點連結
- ✅ 智慧空行處理
- ✅ 依分類自動套用 Footer CTA

### 社群媒體嵌入

支援自動將獨立 URL 轉換為嵌入式卡片:

| 平台 | 支援類型 | 自動高度調整 |
|------|---------|------------|
| Instagram | 圖文、Reels、IGTV | ✅ |
| Threads | 文字、圖片、影片 | ✅ |
| Facebook | 貼文、影片 | ✅ |
| YouTube | 影片 | ✅ |

### 圖片處理

- 🎯 自訂尺寸 (預設 810×540px)
- 📉 JPEG 壓縮 (品質 30-95%)
- 📊 即時預覽和檔案大小顯示

## 🏗️ 架構設計

```
┌─────────────────┐         ┌─────────────────┐
│  Gradio 前端    │  HTTP   │  FastAPI 後端   │
│  (使用者介面)   │ ◄─────► │  (核心處理)     │
│  Port: 7860     │         │  Port: 8000     │
└─────────────────┘         └─────────────────┘
                                    │
                            ┌───────┴───────┐
                            │               │
                      ┌─────▼─────┐   ┌────▼────┐
                      │ Word 處理 │   │ 圖片處理│
                      │   模組    │   │  模組   │
                      └───────────┘   └─────────┘
```

## 🚀 快速開始

### 環境需求

- Python 3.8 或以上
- pip (Python 套件管理器)

### 安裝步驟

#### 1. 克隆專案

```bash
git clone https://github.com/your-username/photonic-filament.git
cd photonic-filament
```

#### 2. 安裝後端依賴

```bash
cd backend
pip install -r requirements.txt
```

#### 3. 安裝前端依賴

```bash
cd ../frontend
pip install -r requirements.txt
```

### 啟動應用

#### 方法一:分別啟動 (開發模式)

**終端機 1 - 啟動後端:**

```bash
cd backend
python app.py
```

後端將在 `http://localhost:8000` 啟動

**終端機 2 - 啟動前端:**

```bash
cd frontend
python app.py
```

前端將在 `http://localhost:7860` 啟動

#### 方法二:使用 Docker Compose (推薦)

```bash
docker-compose up
```

### 使用方式

1. 開啟瀏覽器訪問 `http://localhost:7860`
2. 上傳 Word 文件 (.docx)
3. 選擇文章分類
4. 點擊「開始轉換」
5. 預覽結果並下載 HTML

## 📚 API 文件

### 後端 API 端點

#### 1. Word 轉 HTML

```http
POST /api/convert-docx
Content-Type: multipart/form-data

Parameters:
- file: Word 文件檔案 (.docx)
- category: 文章分類

Response:
{
  "success": true,
  "html": "<html>...</html>",
  "title": "文章主標題",
  "category": "🔵 數據分析解方"
}
```

#### 2. 圖片處理

```http
POST /api/process-image
Content-Type: multipart/form-data

Parameters:
- file: 圖片檔案 (jpg/png/webp)
- width: 目標寬度 (預設 810)
- height: 目標高度 (預設 540)
- quality: 壓縮品質 (預設 70)

Response:
{
  "success": true,
  "image": "data:image/jpeg;base64,...",
  "size_kb": 125.3,
  "info": "✅ 已輸出 810×540,品質 70%｜約 125.3 KB",
  "dimensions": {"width": 810, "height": 540},
  "quality": 70
}
```

#### 3. 健康檢查

```http
GET /health

Response:
{
  "status": "healthy"
}
```

### 互動式 API 文件

後端啟動後,訪問 `http://localhost:8000/docs` 查看完整的 Swagger UI 文件。

## 📁 專案結構

```
photonic-filament/
├── backend/                    # 後端服務
│   ├── app.py                 # FastAPI 主應用
│   ├── core/                  # 核心功能模組
│   │   ├── __init__.py
│   │   ├── word_processor.py # Word 處理
│   │   ├── html_converter.py # HTML 轉換
│   │   └── image_processor.py# 圖片處理
│   ├── templates/             # 模板
│   │   ├── __init__.py
│   │   └── footers.py        # Footer HTML
│   └── requirements.txt       # 後端依賴
├── frontend/                   # 前端服務
│   ├── app.py                 # Gradio 應用
│   ├── config.py              # 配置檔案
│   └── requirements.txt       # 前端依賴
├── README.md                   # 專案說明
├── .gitignore                 # Git 忽略清單
└── docker-compose.yml         # Docker 配置
```

## 🔧 配置說明

### 環境變數

前端可透過環境變數設定後端 API URL:

```bash
# Windows
set BACKEND_URL=http://localhost:8000

# Linux/Mac
export BACKEND_URL=http://localhost:8000
```

### 文章分類

支援以下分類,每個分類對應不同的 Footer CTA:

- 🔵 數據分析解方
- 🔷 產業口碑數據
- 🟦 消費者洞察
- 🩷 網紅行銷策略
- 🟡 社群粉絲團健檢
- 🟣 Threads 行銷服務

## 🚢 部署指南

### 部署到雲端平台

#### Heroku

**後端:**

```bash
cd backend
heroku create your-app-backend
git push heroku main
```

**前端:**

```bash
cd frontend
heroku create your-app-frontend
heroku config:set BACKEND_URL=https://your-app-backend.herokuapp.com
git push heroku main
```

#### Railway / Render

1. 連接 GitHub 儲存庫
2. 分別建立兩個服務 (backend 和 frontend)
3. 設定環境變數 `BACKEND_URL`

### Docker 部署

```bash
# 建立映像
docker-compose build

# 啟動服務
docker-compose up -d

# 查看日誌
docker-compose logs -f
```

## 🛠️ 開發指南

### 新增 Footer 模板

編輯 `backend/templates/footers.py`:

```python
FOOTER_NEW_CATEGORY = """<div>...</div>"""

CATEGORY_TO_FOOTER_HTML = {
    "🆕 新分類": FOOTER_NEW_CATEGORY,
    # ... 其他分類
}
```

### 新增支援的社群平台

編輯 `backend/core/word_processor.py` 中的 `convert_url_to_iframe()` 函數。

## 📝 授權

本專案採用 MIT 授權條款。

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request!

## 📧 聯絡方式

如有問題或建議,請聯絡:

- Email: <your-email@example.com>
- GitHub Issues: [提交問題](https://github.com/your-username/photonic-filament/issues)

---

<div align="center">

**開源專案 · 歡迎貢獻**

</div>
