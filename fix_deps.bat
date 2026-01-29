@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo [修復模式] 正在重置前端套件...

REM 啟用虛擬環境
call .venv\Scripts\activate

REM 強制移除 gradio
echo [1/3] 移除舊版套件...
pip uninstall -y gradio
pip uninstall -y gradio-client

REM 清理快取
pip cache purge

REM 安裝指定穩定版本
echo [2/3] 重新安裝穩定版...
pip install "gradio>=4.44.1,<5.0.0" 
REM 暫時用 4.x 後期版本，因為 5.x 可能在 Python 3.14 上有問題

echo [3/3] 驗證安裝...
python -c "import gradio; print(gradio.__version__)"

echo 修復完成！請按任意鍵退出，然後再次執行 start.bat
pause
