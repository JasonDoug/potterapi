from __future__ import annotations

from app.main import app


for route in app.routes:
    print(f"- {route.path}")
