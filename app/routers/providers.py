from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, AnyUrl, Field


router = APIRouter(tags=["Providers"])


# Data loading utilities
REPO_ROOT = Path(__file__).resolve().parents[2]
PROVIDERS_JSON = REPO_ROOT / "providers" / "examples" / "providers.json"
CAPABILITIES_JSON = REPO_ROOT / "providers" / "examples" / "capabilities.json"


class Provider(BaseModel):
    id: str
    name: str
    category: str
    description: str | None = None
    url: AnyUrl | None = None
    status: str = Field("active", pattern=r"^(active|inactive)$")


class Capability(BaseModel):
    id: str
    name: str
    type: str
    input_schema: str | None = None
    output_schema: str | None = None


def _load_json(path: Path) -> Any:
    import json

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _all_providers() -> List[Provider]:
    data = _load_json(PROVIDERS_JSON)
    return [Provider(**p) for p in data]


def _all_capabilities() -> List[Capability]:
    data = _load_json(CAPABILITIES_JSON)
    return [Capability(**c) for c in data]


# Optional, simple mapping so some providers expose a subset.
CAPABILITY_MAP: Dict[str, List[str]] = {
    # OpenRouter focuses on text generation
    "openrouter": ["text-gen"],
    # others fall back to all capabilities for now
}


@router.get("/providers", response_model=List[Provider])
async def list_providers() -> List[Provider]:
    return _all_providers()


@router.get("/providers/{id}", response_model=Provider)
async def get_provider(id: str) -> Provider:
    for p in _all_providers():
        if p.id == id:
            return p
    raise HTTPException(status_code=404, detail={"error": "not_found", "message": f"Provider '{id}' not found"})


@router.get("/providers/{id}/capabilities", response_model=List[Capability])
async def list_capabilities(id: str) -> List[Capability]:
    # Validate provider exists
    _ = await get_provider(id)

    caps = _all_capabilities()
    names = CAPABILITY_MAP.get(id)
    if names:
        return [c for c in caps if c.id in names]
    return caps
