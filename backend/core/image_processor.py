"""
圖片處理核心模組
負責圖片的 resize 和壓縮處理
"""

from PIL import Image
import io
import os


def process_image(image_bytes: bytes, width: int = 810, height: int = 540, quality: int = 70):
    """
    處理圖片:調整大小和壓縮
    
    Args:
        image_bytes: 原始圖片的位元組資料
        width: 目標寬度 (預設 810px)
        height: 目標高度 (預設 540px)
        quality: JPEG 壓縮品質 (預設 70%)
        
    Returns:
        tuple: (processed_image_bytes, file_size_kb, info_message)
            - processed_image_bytes: 處理後的圖片位元組資料
            - file_size_kb: 檔案大小 (KB)
            - info_message: 處理資訊訊息
    """
    # 開啟圖片
    img = Image.open(io.BytesIO(image_bytes))
    img = img.convert("RGB")
    
    # 調整大小
    img_resized = img.resize((width, height), Image.LANCZOS)
    
    # 壓縮並儲存到記憶體
    output = io.BytesIO()
    img_resized.save(output, format="JPEG", quality=quality, optimize=True)
    output.seek(0)
    
    # 計算檔案大小
    processed_bytes = output.getvalue()
    size_kb = len(processed_bytes) / 1024
    
    info = f"✅ 已輸出 {width}×{height},品質 {quality}%｜約 {size_kb:.1f} KB"
    
    return processed_bytes, size_kb, info
