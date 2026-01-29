#!/bin/bash
# i-Buzz Editor 快速啟動腳本 (Linux/Mac)
# 此腳本會同時啟動後端和前端服務

echo "========================================"
echo "  i-Buzz Editor 啟動中..."
echo "========================================"
echo ""

# 檢查是否在正確的目錄
if [ ! -f "backend/app.py" ]; then
    echo "[錯誤] 請在專案根目錄執行此腳本"
    exit 1
fi

# 啟動後端
echo "[1/2] 啟動後端服務 (Port 8000)..."
cd backend
python app.py &
BACKEND_PID=$!
cd ..

# 等待後端啟動
sleep 3

# 啟動前端
echo "[2/2] 啟動前端服務 (Port 7860)..."
cd frontend
python app.py &
FRONTEND_PID=$!
cd ..

echo ""
echo "========================================"
echo "  啟動完成!"
echo "========================================"
echo ""
echo "後端 API: http://localhost:8000"
echo "前端介面: http://localhost:7860"
echo "API 文件: http://localhost:8000/docs"
echo ""
echo "按 Ctrl+C 停止所有服務"

# 等待中斷信號
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
