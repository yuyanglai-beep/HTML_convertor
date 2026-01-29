@echo off
chcp 65001
cd /d "%~dp0"
echo =================================
echo   前端診斷模式 (Debug Frontend)
echo =================================

echo [1/2] 啟用虛擬環境...
call .venv\Scripts\activate
if %errorlevel% neq 0 (
    echo [ERROR] 虛擬環境啟用失敗!
    pause
    exit /b
)
echo 虛擬環境已啟用。
echo.

echo [2/2] 嘗試啟動前端應用程式...
echo ---------------------------------
cd frontend
python app.py

echo.
echo =================================
echo   前端程式執行結束 (如果有錯誤請截圖)
echo =================================
pause
