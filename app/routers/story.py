from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Body, status, Depends

from ..utils.validation import validate_body, load_schema_from_openapi
from ..utils.stubgen import generate_stub
from ..config import Settings, get_settings
from ..utils.common import _read_json, _maybe_example

router = APIRouter(prefix="/v1", tags=["Story"])


def _response_from_schema(schema_name: str, settings: Settings) -> Any:
    schema = load_schema_from_openapi(settings.STORY_OPENAPI_FILE, schema_name)
    return generate_stub(schema)


@router.post("/storyboards", status_code=status.HTTP_201_CREATED)
async def create_storyboard(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    schema = load_schema_from_openapi(settings.STORY_OPENAPI_FILE, "StoryboardCreateRequest")
    validate_body(payload, schema)
    example = _maybe_example("storyboard.create", settings.STORY_EXAMPLES_PATH)
    if example is not None:
        return example
    return _response_from_schema("Storyboard", settings)


@router.get("/storyboards/{storyboard_id}")
async def get_storyboard(storyboard_id: str, settings: Settings = Depends(get_settings)) -> Any:
    data = _response_from_schema("Storyboard", settings)
    if isinstance(data, dict):
        data.setdefault("id", storyboard_id)
        data.setdefault("status", "succeeded")
    return data


@router.post("/storyboards/{storyboard_id}/render", status_code=status.HTTP_202_ACCEPTED)
async def render_storyboard(storyboard_id: str, payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    schema = load_schema_from_openapi(settings.STORY_OPENAPI_FILE, "StoryboardRenderRequest")
    validate_body(payload, schema)
    # This endpoint is not fully defined in the OpenAPI spec, so we'll return a generic response
    return {"message": "Storyboard rendering started", "storyboard_id": storyboard_id}


@router.post("/stories", status_code=status.HTTP_202_ACCEPTED)
async def create_story(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    schema = load_schema_from_openapi(settings.STORY_OPENAPI_FILE, "StoryCreateRequest")
    validate_body(payload, schema)
    example = _maybe_example("story.create", settings.STORY_EXAMPLES_PATH)
    if example is not None:
        return example
    return _response_from_schema("StoryJob", settings)


@router.get("/stories/{story_id}")
async def get_story(story_id: str, settings: Settings = Depends(get_settings)) -> Any:
    data = _response_from_schema("StoryJob", settings)
    if isinstance(data, dict):
        data.setdefault("id", story_id)
        data.setdefault("status", "succeeded")
    return data


@router.get("/stories/{story_id}/videos")
async def get_story_videos(story_id: str) -> Any:
    # This endpoint is not fully defined in the OpenAPI spec, so we'll return a generic response
    return {"items": []}
