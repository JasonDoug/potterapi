from __future__ import annotations

from fastapi import Request, status
from fastapi.responses import JSONResponse


class ProviderNotFoundException(Exception):
    def __init__(self, provider_id: str):
        self.provider_id = provider_id


def provider_not_found_exception_handler(request: Request, exc: ProviderNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": "not_found", "message": f"Provider '{exc.provider_id}' not found"},
    )
