@echo off
REM Word 轉 HTML 工具快速啟動腳本 (Windows)
REM 此腳本會同時啟動後端和前端服務

echo ========================================
echo   Word 轉 HTML 工具啟動中...
echo ========================================
echo.

REM 檢查是否在正確的目錄
if not exist "backend\app.py" (
    echo [錯誤] 請在專案根目錄執行此腳本
    pause
    exit /b 1
)

echo [0/2] 正在檢查並安裝必要的程式庫 (第一次會比較久)...
echo 安裝後端套件...
pip install -r backend\requirements.txt
echo 安裝前端套件...
pip install -r frontend\requirements.txt
echo.

REM 啟動後端 (在新視窗)
echo [1/2] 啟動後端服務 (Port 8000)...
start "Backend" cmd /k "cd backend && python app.py"

REM 等待後端啟動
timeout /t 3 /nobreak > nul

REM 啟動前端 (在新視窗)
echo [2/2] 啟動前端服務 (Port 7860)...
start "Frontend" cmd /k "cd frontend && python app.py"

echo.
echo ========================================
echo   啟動完成!
echo ========================================
echo.
echo 後端 API: http://localhost:8000
echo 前端介面: http://localhost:7860
echo API 文件: http://localhost:8000/docs
echo.
echo 按任意鍵關閉此視窗...
pause > nul
