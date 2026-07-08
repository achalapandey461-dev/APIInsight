from fastapi import APIRouter
import os
import re

router = APIRouter()

# Sirf in file types ko scan karenge
SUPPORTED_FILES = (
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".json",
    ".html",
    ".css",
    ".md"
)

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

            # Sirf supported files hi read karo
            if file.endswith(SUPPORTED_FILES):

                try:
                    file_path = os.path.join(root, file)

                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                        # FastAPI APIs
                        api_counts["GET"] += len(re.findall(r"\.get\(", content))
                        api_counts["POST"] += len(re.findall(r"\.post\(", content))
                        api_counts["PUT"] += len(re.findall(r"\.put\(", content))
                        api_counts["DELETE"] += len(re.findall(r"\.delete\(", content))

                except Exception as e:
                    print(f"Error reading {file}: {e}")

    return {
        "total_apis": sum(api_counts.values()),
        "breakdown": api_counts
    }