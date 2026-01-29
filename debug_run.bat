@echo off
chcp 65001
cd /d "%~dp0"
echo =================================
echo   診斷模式 (Debug Mode)
echo =================================

echo [1/5] 檢查環境變數...
where python
echo.

echo [2/5] 檢查 Python 版本 (Global)...
python --version
py --list
echo.

echo [3/5] 檢查虛擬環境...
if exist ".venv" (
    echo .venv 存在
) else (
    echo [ERROR] .venv 不存在!
    pause
    exit /b
)
echo.

echo [4/5] 啟用虛擬環境...
call .venv\Scripts\activate
if %errorlevel% neq 0 (
    echo [ERROR] 虛擬環境啟用失敗!
    pause
    exit /b
)
echo 虛擬環境已啟用。
echo.

echo [5/5] 檢查 Python 版本 (Venv)...
where python
python --version
echo.

echo ---------------------------------
echo 嘗試啟動後端應用程式...
echo ---------------------------------
cd backend
python app.py

echo.
echo =================================
echo   程式執行結束
echo =================================
pause
