@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Word to HTML - Backend Server

echo [啟動中] 正在啟動後端伺服器...
echo.

if not exist ".venv" (
    echo [錯誤] 找不到虛擬環境 (.venv)
    echo 請先執行 FORCE_REINSTALL.bat
    pause
    exit /b 1
)

call .venv\Scripts\activate
cd backend

echo [執行] python app.py
python app.py

if %errorlevel% neq 0 (
    echo.
    echo [已停止] 伺服器因錯誤而停止。
    pause
)
