"""
前端配置檔案
"""

import os

# 後端 API URL (可透過環境變數覆寫)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
