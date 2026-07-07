from fastapi import APIRouter
import os
import re

router = APIRouter()

@router.get("/scan")
def scan_project():

    api_counts = {
        "GET": 0,
        "POST": 0,
        "PUT": 0,
        "DELETE": 0
    }

    for root, dirs, files in os.walk("extracted"):
        for file in files:

            if file.endswith(".py"):

                try:
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        content = f.read()

                        # 🔥 Improved patterns
                        api_counts["GET"] += len(re.findall(r'\.get\(', content))
                        api_counts["POST"] += len(re.findall(r'\.post\(', content))
                        api_counts["PUT"] += len(re.findall(r'\.put\(', content))
                        api_counts["DELETE"] += len(re.findall(r'\.delete\(', content))

                except:
                    pass

    return {
        "total_apis": sum(api_counts.values()),
        "breakdown": api_counts
    }