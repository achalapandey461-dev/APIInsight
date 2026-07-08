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

    api_endpoints = []

    for root, dirs, files in os.walk("extracted"):

        for file in files:

            if file.endswith(".py"):

                try:
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        content = f.read()

                        # Find API routes
                        get_routes = re.findall(r'@router\.get\("([^"]+)"\)', content)
                        post_routes = re.findall(r'@router\.post\("([^"]+)"\)', content)
                        put_routes = re.findall(r'@router\.put\("([^"]+)"\)', content)
                        delete_routes = re.findall(r'@router\.delete\("([^"]+)"\)', content)

                        # Count APIs
                        api_counts["GET"] += len(get_routes)
                        api_counts["POST"] += len(post_routes)
                        api_counts["PUT"] += len(put_routes)
                        api_counts["DELETE"] += len(delete_routes)

                        # Store endpoint details
                        for route in get_routes:
                            api_endpoints.append({
                                "method": "GET",
                                "path": route
                            })

                        for route in post_routes:
                            api_endpoints.append({
                                "method": "POST",
                                "path": route
                            })

                        for route in put_routes:
                            api_endpoints.append({
                                "method": "PUT",
                                "path": route
                            })

                        for route in delete_routes:
                            api_endpoints.append({
                                "method": "DELETE",
                                "path": route
                            })

                except Exception:
                    pass

    return {
        "total_apis": sum(api_counts.values()),
        "breakdown": api_counts,
        "endpoints": api_endpoints
    }