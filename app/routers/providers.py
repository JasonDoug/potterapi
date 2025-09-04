from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Any

from fastapi import APIRouter, Depends
from pydantic import BaseModel, AnyUrl, Field

from ..config import Settings, get_settings
from ..exceptions import ProviderNotFoundException

router = APIRouter(tags=["Providers"])


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


def _all_providers(settings: Settings) -> List[Provider]:
    data = _load_json(settings.PROVIDERS_EXAMPLES_PATH / "providers.json")
    return [Provider(**p) for p in data]


def _all_capabilities(settings: Settings) -> List[Capability]:
    data = _load_json(settings.PROVIDERS_EXAMPLES_PATH / "capabilities.json")
    return [Capability(**c) for c in data]


# Optional, simple mapping so some providers expose a subset.
CAPABILITY_MAP: Dict[str, List[str]] = {
    # OpenRouter focuses on text generation
    "openrouter": ["text-gen"],
    # others fall back to all capabilities for now
}


@router.get("/providers", response_model=List[Provider])
async def list_providers(settings: Settings = Depends(get_settings)) -> List[Provider]:
    return _all_providers(settings)


@router.get("/providers/{id}", response_model=Provider)
async def get_provider(id: str, settings: Settings = Depends(get_settings)) -> Provider:
    for p in _all_providers(settings):
        if p.id == id:
            return p
    raise ProviderNotFoundException(id)


@router.get("/providers/{id}/capabilities", response_model=List[Capability])
async def list_capabilities(id: str, settings: Settings = Depends(get_settings)) -> List[Capability]:
    # Validate provider exists
    await get_provider(id, settings)

    caps = _all_capabilities(settings)
    names = CAPABILITY_MAP.get(id)
    if names:
        return [c for c in caps if c.id in names]
    return caps
