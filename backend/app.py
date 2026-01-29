"""
FastAPI 後端應用
提供 Word 轉 HTML 和圖片處理的 REST API
"""

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import tempfile
import os
from typing import Optional

from core.html_converter import docx_to_html_with_links
from core.image_processor import process_image

# 建立 FastAPI 應用
app = FastAPI(
    title="i-Buzz Editor API",
    description="Word 轉 HTML 和圖片處理 API",
    version="1.0.0"
)

# 設定 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生產環境應該限制特定來源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """根路徑"""
    return {
        "message": "i-Buzz Editor API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "convert_docx": "/api/convert-docx",
            "process_image": "/api/process-image",
            "docs": "/docs"
        }
    }


@app.get("/health")
async def health_check():
    """健康檢查端點"""
    return {"status": "healthy"}


@app.post("/api/convert-docx")
async def convert_docx(
    file: UploadFile = File(..., description="Word 文件檔案 (.docx)"),
    category: str = Form(..., description="文章分類")
):
    """
    將 Word 文件轉換為 HTML
    
    Args:
        file: Word 文件檔案
        category: 文章分類 (決定 Footer 樣式)
        
    Returns:
        JSON 格式的轉換結果,包含 HTML 內容和主標題
    """
    # 驗證檔案類型
    if not file.filename.endswith('.docx'):
        raise HTTPException(status_code=400, detail="只支援 .docx 格式的檔案")
    
    try:
        # 儲存上傳的檔案到臨時位置
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name
        
        # 執行轉換
        html_content, h1_title = docx_to_html_with_links(tmp_path, category)
        
        # 刪除臨時檔案
        os.unlink(tmp_path)
        
        return JSONResponse(content={
            "success": True,
            "html": html_content,
            "title": h1_title,
            "category": category
        })
    
    except Exception as e:
        # 確保臨時檔案被刪除
        if 'tmp_path' in locals() and os.path.exists(tmp_path):
            os.unlink(tmp_path)
        
        raise HTTPException(status_code=500, detail=f"轉換失敗: {str(e)}")


@app.post("/api/process-image")
async def process_image_endpoint(
    file: UploadFile = File(..., description="圖片檔案 (jpg/png/webp)"),
    width: Optional[int] = Form(810, description="目標寬度"),
    height: Optional[int] = Form(540, description="目標高度"),
    quality: Optional[int] = Form(70, description="JPEG 壓縮品質 (30-95)")
):
    """
    處理圖片:調整大小和壓縮
    
    Args:
        file: 圖片檔案
        width: 目標寬度 (預設 810px)
        height: 目標高度 (預設 540px)
        quality: JPEG 壓縮品質 (預設 70%)
        
    Returns:
        JSON 格式的處理結果,包含處理後的圖片 (base64) 和檔案資訊
    """
    # 驗證檔案類型
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.webp']
    if not any(file.filename.lower().endswith(ext) for ext in allowed_extensions):
        raise HTTPException(status_code=400, detail="只支援 jpg, png, webp 格式的圖片")
    
    # 驗證參數範圍
    if quality < 30 or quality > 95:
        raise HTTPException(status_code=400, detail="品質參數必須在 30-95 之間")
    
    if width <= 0 or height <= 0:
        raise HTTPException(status_code=400, detail="寬度和高度必須大於 0")
    
    try:
        # 讀取圖片
        image_bytes = await file.read()
        
        # 處理圖片
        processed_bytes, size_kb, info = process_image(image_bytes, width, height, quality)
        
        # 將處理後的圖片轉為 base64
        import base64
        image_base64 = base64.b64encode(processed_bytes).decode('utf-8')
        
        return JSONResponse(content={
            "success": True,
            "image": f"data:image/jpeg;base64,{image_base64}",
            "size_kb": round(size_kb, 1),
            "info": info,
            "dimensions": {
                "width": width,
                "height": height
            },
            "quality": quality
        })
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"圖片處理失敗: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
