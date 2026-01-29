# 🚀 GitHub 快速部署指令

## 步驟 1: 建立 GitHub 儲存庫

點擊以下連結,會自動填好所有欄位:

👉 **[點我建立儲存庫](https://github.com/new?name=HTML_convertor&description=Word+轉+HTML+工具&visibility=public)**

在開啟的頁面中:

1. 確認資訊無誤
2. **不要**勾選任何選項 (README、.gitignore、License)
3. 點擊綠色的 **"Create repository"** 按鈕

---

## 步驟 2: 複製你的儲存庫 URL

建立完成後,GitHub 會顯示一個頁面,上面有你的儲存庫 URL。

URL 格式會像這樣:

```
https://github.com/你的使用者名稱/HTML_convertor.git
```

**請複製這個 URL!**

---

## 步驟 3: 推送程式碼到 GitHub

### 方法 A: 使用下方的指令 (推薦)

在下方的 PowerShell 視窗中執行以下指令:

```powershell
# 進入專案目錄
cd c:\Users\yuyan\.gemini\antigravity\playground\photonic-filament

# 添加遠端儲存庫 (請替換成你的 URL)
git remote add origin https://github.com/你的使用者名稱/HTML_convertor.git

# 重新命名分支為 main
git branch -M main

# 推送程式碼
git push -u origin main
```

### 方法 B: 讓我幫你執行

如果你把你的 GitHub 使用者名稱告訴我,我可以直接幫你執行這些指令!

例如,如果你的使用者名稱是 `yuyan123`,請告訴我,我會自動執行:

```
git remote add origin https://github.com/yuyan123/HTML_convertor.git
git push -u origin main
```

---

## 步驟 4: 驗證部署

推送完成後:

1. 重新整理你的 GitHub 儲存庫頁面
2. 你應該會看到所有檔案都已上傳
3. README.md 會自動顯示專案說明

---

## 🔐 如果需要登入

第一次推送時,Git 可能會要求你登入 GitHub:

### Windows 使用者

- 會彈出 GitHub 登入視窗
- 使用你的 GitHub 帳號密碼登入
- 或使用 Personal Access Token

### 如何建立 Personal Access Token

1. 訪問 <https://github.com/settings/tokens>
2. 點擊 "Generate new token" → "Generate new token (classic)"
3. 勾選 `repo` 權限
4. 點擊 "Generate token"
5. **複製 token** (只會顯示一次!)
6. 在 Git 要求密碼時,貼上這個 token

---

## ❓ 常見問題

### Q: 出現 "remote origin already exists" 錯誤?

執行:

```powershell
git remote remove origin
git remote add origin https://github.com/你的使用者名稱/HTML_convertor.git
```

### Q: 推送失敗?

檢查:

1. 網路連線是否正常
2. GitHub 使用者名稱是否正確
3. 是否有權限推送到該儲存庫

---

## 📞 需要協助?

請告訴我:

1. 你的 GitHub 使用者名稱
2. 遇到的錯誤訊息 (如果有)

我會立即協助你解決!
