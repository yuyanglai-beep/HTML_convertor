@echo off
setlocal
cd /d "%~dp0"

echo ===================================================
echo   Word 轉 HTML 工具 - 自動安裝與啟動腳本 (v2)
echo ===================================================

REM 1. 檢查 Python 是否存在
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [錯誤] 找不到 Python! 請先安裝 Python，並記得勾選 "Add Python to PATH"。
    pause
    exit /b 1
)

REM 2. 建立虛擬環境 (如果不存在)
if not exist ".venv" (
    echo [1/3] 正在建立虛擬環境 (這會確保你的電腦乾淨)...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo [錯誤] 建立虛擬環境失敗。
        pause
        exit /b 1
    )
)

REM 3. 啟用虛擬環境並安裝套件
echo [2/3] 正在檢查與安裝套件...
call .venv\Scripts\activate

REM 升級 pip
python -m pip install --upgrade pip >nul 2>&1

REM 安裝後端
echo     - 安裝後端需求...
python -m pip install -r backend\requirements.txt >nul
if %errorlevel% neq 0 (
    echo [錯誤] 後端套件安裝失敗！
    pause
    exit /b 1
)

REM 安裝前端
echo     - 安裝前端需求...
python -m pip install -r frontend\requirements.txt >nul
if %errorlevel% neq 0 (
    echo [錯誤] 前端套件安裝失敗！
    pause
    exit /b 1
)

echo [完成] 所有套件安裝完畢。
echo.

REM 4. 啟動服務
echo [3/3] 啟動服務中...
echo.

REM 啟動後端 (使用虛擬環境)
start "Backend API" cmd /k "call .venv\Scripts\activate && cd backend && python app.py"

REM 等待後端初始化
timeout /t 3 /nobreak >nul

REM 啟動前端 (使用虛擬環境)
start "Frontend UI" cmd /k "call .venv\Scripts\activate && cd frontend && python app.py"

echo ===================================================
echo   服務已在新的視窗中啟動!
echo.
echo   - 後端: http://localhost:8000
echo   - 前端: http://localhost:7860
echo.
echo   您可以縮小此視窗 (請勿關閉新跳出的視窗)
echo ===================================================
pause
