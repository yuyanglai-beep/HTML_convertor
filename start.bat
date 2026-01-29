@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ===================================================
echo   Word 轉 HTML 工具 - 啟動器
echo ===================================================
echo.

if not exist ".venv" (
    echo [警告] 尚未發現虛擬環境，可能尚未執行修復。
    echo 請先執行 FORCE_REINSTALL.bat
    echo.
    echo 按任意鍵繼續嘗試啟動...
    pause >nul
)

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
