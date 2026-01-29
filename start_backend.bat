@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Word to HTML - Backend Server

echo [啟動中] 正在啟動後端伺服器...
echo.

echo 目前工作目錄: %cd%

REM 直接嘗試啟用虛擬環境
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate
) else (
    echo [警告] 找不到 .venv\Scripts\activate.bat，嘗試直接執行...
)
cd backend

echo [執行] python app.py
python app.py

if %errorlevel% neq 0 (
    echo.
    echo [已停止] 伺服器因錯誤而停止。
    pause
)
