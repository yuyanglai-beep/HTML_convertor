@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ===================================================
echo   Word 轉 HTML 工具 - 啟動器
echo ===================================================
echo.

REM 移除虛擬環境硬性檢查，交由子腳本處理
echo [檢查] 準備啟動相關服務 (後端 + 前端)
echo.

echo [1/2] 正在啟動後端視窗...
start "WordToHTML_Backend" cmd /c "start_backend.bat"

echo [2/2] 正在啟動前端視窗...
timeout /t 2 /nobreak >nul
start "WordToHTML_Frontend" cmd /c "start_frontend.bat"

echo.
echo ===================================================
echo   已發送啟動指令！
echo.
echo   請查看新跳出的兩個視窗。
echo   如果視窗沒有出現，請直接手動執行:
echo     1. start_backend.bat
echo     2. start_frontend.bat
echo ===================================================
pause
