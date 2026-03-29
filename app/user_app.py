from fastapi import APIRouter

router = APIRouter()

# ============================================================
# PUT YOUR TUTORIAL ROUTES HERE
# ============================================================
# This router is mounted at /app/*
# Example URLs:
#   GET /app/portfolio
#   GET /app/items
#
# Rules:
# - Never put /health here.
# - Keep /health only in app/core.py.
# ============================================================

@router.get("/portfolio")
def portfolio_placeholder():
    return {
        "name": "Liam",
        "title": "Portfolio Placeholder",
        "projects": [
            {"name": "DevOps Practice ECS", "status": "in progress"}
        ]
    }