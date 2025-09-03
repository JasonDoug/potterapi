from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Body, status, Depends

from ..utils.validation import validate_body, load_schema_from_openapi
from ..utils.stubgen import generate_stub
from ..config import Settings, get_settings
from ..utils.common import _read_json, _maybe_example

router = APIRouter(prefix="/v1", tags=["Video"])


def _response_from_schema(schema_name: str, settings: Settings) -> Any:
    schema = load_schema_from_openapi(settings.STORY_OPENAPI_FILE, schema_name)
    return generate_stub(schema)


@router.post("/videos", status_code=status.HTTP_202_ACCEPTED)
async def create_video(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    schema = load_schema_from_openapi(settings.STORY_OPENAPI_FILE, "VideoCreateRequest")
    validate_body(payload, schema)
    example = _maybe_example("video.create", settings.STORY_EXAMPLES_PATH)
    if example is not None:
        return example
    return _response_from_schema("VideoJob", settings)


@router.get("/videos/{video_id}")
async def get_video(video_id: str, settings: Settings = Depends(get_settings)) -> Any:
    data = _response_from_schema("VideoJob", settings)
    if isinstance(data, dict):
        data.setdefault("id", video_id)
        data.setdefault("status", "succeeded")
    return data
