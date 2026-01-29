# GitHub 部署指南

## 📋 前置準備

1. **GitHub 帳號**: 確保你有 GitHub 帳號
2. **Git 已安裝**: 確認本機已安裝 Git
3. **程式碼已提交**: 本地 Git 儲存庫已初始化並提交

## 🚀 部署步驟

### 步驟 1: 在 GitHub 建立新儲存庫

1. 登入 [GitHub](https://github.com)
2. 點擊右上角的 `+` → `New repository`
3. 填寫儲存庫資訊:
   - **Repository name**: `HTML_convertor` (或你喜歡的名稱)
   - **Description**: `i-Buzz Editor - Word 轉 HTML 工具`
   - **Visibility**: 選擇 Public 或 Private
   - **不要**勾選 "Initialize this repository with a README"
4. 點擊 `Create repository`

### 步驟 2: 連接本地儲存庫到 GitHub

複製 GitHub 提供的儲存庫 URL,然後在本地執行:

```bash
# 進入專案目錄
cd c:\Users\yuyan\.gemini\antigravity\playground\photonic-filament

# 添加遠端儲存庫 (替換成你的 GitHub URL)
git remote add origin https://github.com/your-username/HTML_convertor.git

# 推送程式碼到 GitHub
git branch -M main
git push -u origin main
```

### 步驟 3: 驗證部署

1. 重新整理 GitHub 儲存庫頁面
2. 確認所有檔案都已成功上傳
3. 檢查 README.md 是否正確顯示

## 📝 後續更新流程

當你修改程式碼後,使用以下命令推送更新:

```bash
# 查看修改狀態
git status

# 添加所有修改
git add .

# 提交修改
git commit -m "描述你的修改內容"

# 推送到 GitHub
git push
```

## 🌐 部署到雲端平台

### 選項 1: Render (推薦,免費方案)

#### 部署後端

1. 登入 [Render](https://render.com)
2. 點擊 `New` → `Web Service`
3. 連接你的 GitHub 儲存庫
4. 設定:
   - **Name**: `ibuzz-backend`
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
5. 點擊 `Create Web Service`
6. 複製部署後的 URL (例如: `https://ibuzz-backend.onrender.com`)

#### 部署前端

1. 在 Render 點擊 `New` → `Web Service`
2. 連接同一個 GitHub 儲存庫
3. 設定:
   - **Name**: `ibuzz-frontend`
   - **Root Directory**: `frontend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
4. 在 `Environment Variables` 添加:
   - Key: `BACKEND_URL`
   - Value: `https://ibuzz-backend.onrender.com` (你的後端 URL)
5. 點擊 `Create Web Service`

### 選項 2: Railway

1. 登入 [Railway](https://railway.app)
2. 點擊 `New Project` → `Deploy from GitHub repo`
3. 選擇你的儲存庫
4. Railway 會自動偵測並部署兩個服務
5. 設定環境變數 `BACKEND_URL` 指向後端服務

### 選項 3: Heroku

#### 部署後端

```bash
cd backend
heroku login
heroku create ibuzz-backend
git subtree push --prefix backend heroku main
```

#### 部署前端

```bash
cd frontend
heroku create ibuzz-frontend
heroku config:set BACKEND_URL=https://ibuzz-backend.herokuapp.com
git subtree push --prefix frontend heroku main
```

## 🐳 使用 Docker 部署

如果你的雲端平台支援 Docker:

```bash
# 建立並推送 Docker 映像
docker-compose build
docker tag photonic-filament_backend your-registry/ibuzz-backend
docker tag photonic-filament_frontend your-registry/ibuzz-frontend
docker push your-registry/ibuzz-backend
docker push your-registry/ibuzz-frontend
```

## 🔧 環境變數設定

### 後端環境變數

目前後端不需要特殊環境變數,但你可以添加:

- `PORT`: 服務端口 (雲端平台通常自動設定)
- `ALLOWED_ORIGINS`: CORS 允許的來源 (生產環境建議限制)

### 前端環境變數

**必須設定**:

- `BACKEND_URL`: 後端 API 的完整 URL

**可選設定**:

- `GRADIO_SERVER_NAME`: 伺服器名稱 (預設 `0.0.0.0`)
- `GRADIO_SERVER_PORT`: 伺服器端口 (預設 `7860`)

## 📊 監控與維護

### 查看日誌

**Render**:

- 在服務頁面點擊 `Logs` 標籤

**Railway**:

- 在專案頁面點擊服務查看日誌

**Heroku**:

```bash
heroku logs --tail -a ibuzz-backend
heroku logs --tail -a ibuzz-frontend
```

### 效能優化建議

1. **啟用快取**: 考慮使用 Redis 快取常用轉換結果
2. **CDN**: 使用 CDN 加速靜態資源載入
3. **負載平衡**: 高流量時考慮多實例部署
4. **監控**: 使用 Sentry 或 LogRocket 監控錯誤

## 🔒 安全性建議

1. **API 認證**: 生產環境建議加入 API Key 驗證
2. **CORS 限制**: 限制 `allow_origins` 為特定網域
3. **檔案大小限制**: 設定上傳檔案大小上限
4. **速率限制**: 使用 slowapi 限制 API 請求頻率

## ❓ 常見問題

### Q: 前端無法連接後端?

**A**: 檢查:

1. `BACKEND_URL` 環境變數是否正確設定
2. 後端服務是否正常運行
3. CORS 設定是否允許前端網域

### Q: 部署後轉換失敗?

**A**: 檢查:

1. 後端日誌中的錯誤訊息
2. 檔案上傳大小是否超過限制
3. 依賴套件是否正確安裝

### Q: 如何更新已部署的應用?

**A**:

1. 在本地修改程式碼
2. 提交並推送到 GitHub
3. 大多數平台會自動重新部署
4. 或手動觸發重新部署

## 📞 技術支援

如遇到問題:

1. 查看 [README.md](../README.md) 的完整文件
2. 在 GitHub 提交 [Issue](https://github.com/your-username/HTML_convertor/issues)
3. 聯絡開發團隊

---

**祝部署順利! 🎉**
