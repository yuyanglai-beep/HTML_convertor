@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ===================================================
echo   強制重裝與修復工具 (Python 3.12 版)
echo ===================================================
echo.

echo [0/4] 強制結束所有 Python 程序 (釋放檔案鎖定)...
taskkill /F /IM python.exe /T >nul 2>&1
REM 這裡可能會顯示錯誤如果沒有執行中的 python，這是正常的，所以我們隱藏輸出

timeout /t 2 /nobreak >nul

echo [1/4] 清除舊的虛擬環境 (刪除 .venv)...
if exist ".venv" (
    rd /s /q ".venv"
    echo     - 舊環境已刪除
) else (
    echo     - 未發現舊環境，略過
)

echo.
echo [2/4] 使用 Python 3.12 建立新環境...
py -3.12 -m venv .venv
if %errorlevel% neq 0 (
    echo.
    echo [嚴重錯誤] 無法使用 Python 3.12 建立環境！
    echo 請確認你真的有安裝 Python 3.12 並且勾選 "Add to PATH"。
    pause
    exit /b 1
)

echo.
echo [3/4] 安裝相容的套件...
call .venv\Scripts\activate

REM 更新 pip
python -m pip install --upgrade pip

REM 安裝後端
echo     - 安裝後端...
python -m pip install -r backend\requirements.txt

REM 安裝前端
echo     - 安裝前端...
python -m pip install -r frontend\requirements.txt

echo.
echo [4/4] 驗證安裝...
python -c "import gradio; print('Gradio version:', gradio.__version__)"
python -c "import PIL; print('Pillow version:', PIL.__version__)"

echo.
echo ===================================================
echo   修復完成！現在請關閉此視窗，並執行 start.bat
echo ===================================================
pause
