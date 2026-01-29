# 🔄 GitHub 儲存庫重新命名指南

## 步驟 1: 在 GitHub 上重新命名儲存庫

1. **訪問你的儲存庫設定頁面**

   點擊以下連結直接前往:
   👉 **<https://github.com/yuyanglai-beep/ibuzz-editor/settings>**

2. **修改儲存庫名稱**

   - 在頁面最上方找到 **Repository name** 欄位
   - 將名稱從 `ibuzz-editor` 改為 `html-convertor`
   - 點擊 **Rename** 按鈕

3. **確認重新命名**

   GitHub 會顯示警告訊息,點擊確認即可。

---

## 步驟 2: 更新本地 Git 遠端 URL

重新命名後,你需要更新本地專案的遠端 URL。

### 自動執行 (推薦)

我已經為你準備好指令,請執行:

```bash
cd c:\Users\yuyan\.gemini\antigravity\playground\photonic-filament
git remote set-url origin https://github.com/yuyanglai-beep/html-convertor.git
```

### 驗證更新

執行以下指令確認:

```bash
git remote -v
```

應該會顯示:

```
origin  https://github.com/yuyanglai-beep/html-convertor.git (fetch)
origin  https://github.com/yuyanglai-beep/html-convertor.git (push)
```

---

## 步驟 3: 測試推送

執行一次推送測試:

```bash
git push origin main
```

如果成功,表示設定正確!

---

## ⚠️ 注意事項

1. **舊連結會自動重新導向**
   - GitHub 會自動將 `ibuzz-editor` 重新導向到 `html-convertor`
   - 但建議更新所有文件中的連結

2. **其他協作者**
   - 如果有其他人 clone 了這個專案,他們也需要更新遠端 URL

3. **已部署的服務**
   - 如果你有部署到雲端平台,可能需要更新連結

---

## 📝 需要我幫忙嗎?

完成步驟 1 後,告訴我一聲,我會立即幫你執行步驟 2 的指令!
