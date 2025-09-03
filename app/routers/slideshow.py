from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Body, status, Depends

from ..utils.validation import validate_body, load_schema
from ..utils.stubgen import generate_stub
from ..config import Settings, get_settings
from ..utils.common import _read_json, _maybe_example

router = APIRouter(prefix="/v1", tags=["Slideshow"])


def _response_from_schema(schema_file: str, settings: Settings) -> Any:
    schema = load_schema(settings.SLIDESHOW_SCHEMAS_PATH / schema_file)
    return generate_stub(schema)


@router.post("/scripts", status_code=status.HTTP_201_CREATED)
async def create_script(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    validate_body(payload, settings.SLIDESHOW_SCHEMAS_PATH / "ScriptCreate.json")
    example = _maybe_example("scripts.create", settings.SLIDESHOW_EXAMPLES_PATH)
    if example is not None:
        return example
    return _response_from_schema("Script.json", settings)


@router.get("/scripts")
async def list_scripts() -> Any:
    # Minimal list stub conforms to ListResponseScripts
    return {"items": []}


@router.get("/scripts/{script_id}")
async def get_script(script_id: str, settings: Settings = Depends(get_settings)) -> Any:
    data = _response_from_schema("Script.json", settings)
    if isinstance(data, dict):
        data.setdefault("id", script_id)
        data.setdefault("status", "succeeded")
        data.setdefault("created_at", "1970-01-01T00:00:00Z")
        data.setdefault("sections", [])
    return data


@router.post("/beats", status_code=status.HTTP_201_CREATED)
async def create_beats(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    validate_body(payload, settings.SLIDESHOW_SCHEMAS_PATH / "BeatsCreate.json")
    example = _maybe_example("beats.create", settings.SLIDESHOW_EXAMPLES_PATH)
    if example is not None:
        return example
    return _response_from_schema("Beats.json", settings)


@router.get("/beats")
async def list_beats() -> Any:
    # No explicit list schema; return empty for now
    return {"items": []}


@router.post("/images", status_code=status.HTTP_202_ACCEPTED)
async def create_images(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    validate_body(payload, settings.SLIDESHOW_SCHEMAS_PATH / "ImageCreate.json")
    example = _maybe_example("images.create", settings.SLIDESHOW_EXAMPLES_PATH)
    if example is not None:
        return example
    return _response_from_schema("ImageJob.json", settings)


@router.get("/images")
async def list_images() -> Any:
    return {"items": []}


@router.get("/images/{image_job_id}")
async def get_image_job(image_job_id: str, settings: Settings = Depends(get_settings)) -> Any:
    data = _response_from_schema("ImageJob.json", settings)
    if isinstance(data, dict):
        data.setdefault("id", image_job_id)
        data.setdefault("status", "succeeded")
    return data


@router.post("/voiceovers", status_code=status.HTTP_202_ACCEPTED)
async def create_voiceovers(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    validate_body(payload, settings.SLIDESHOW_SCHEMAS_PATH / "VoiceoverCreate.json")
    example = _maybe_example("voiceovers.create", settings.SLIDESHOW_EXAMPLES_PATH)
    if example is not None:
        return example
    return _response_from_schema("VoiceoverJob.json", settings)


@router.get("/voiceovers")
async def list_voiceovers() -> Any:
    return {"items": []}


@router.get("/voiceovers/{voiceover_id}")
async def get_voiceover(voiceover_id: str, settings: Settings = Depends(get_settings)) -> Any:
    data = _response_from_schema("VoiceoverJob.json", settings)
    if isinstance(data, dict):
        data.setdefault("id", voiceover_id)
        data.setdefault("status", "succeeded")
    return data


@router.post("/background-music", status_code=status.HTTP_202_ACCEPTED)
async def create_background_music(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    validate_body(payload, settings.SLIDESHOW_SCHEMAS_PATH / "BackgroundMusicCreate.json")
    example = _maybe_example("background-music.create", settings.SLIDESHOW_EXAMPLES_PATH)
    if example is not None:
        return example
    return _response_from_schema("BackgroundMusicJob.json", settings)


@router.get("/background-music/{music_id}")
async def get_background_music(music_id: str, settings: Settings = Depends(get_settings)) -> Any:
    data = _response_from_schema("BackgroundMusicJob.json", settings)
    if isinstance(data, dict):
        data.setdefault("id", music_id)
        data.setdefault("status", "succeeded")
    return data


@router.post("/slideshows", status_code=status.HTTP_201_CREATED)
async def create_slideshows(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    validate_body(payload, settings.SLIDESHOW_SCHEMAS_PATH / "SlideshowCreate.json")
    example = _maybe_example("slideshows.create", settings.SLIDESHOW_EXAMPLES_PATH)
    if example is not None:
        return example
    return _response_from_schema("Slideshow.json", settings)


@router.get("/slideshows")
async def list_slideshows() -> Any:
    return {"items": []}


@router.get("/slideshows/{slideshow_id}")
async def get_slideshow(slideshow_id: str, settings: Settings = Depends(get_settings)) -> Any:
    data = _response_from_schema("Slideshow.json", settings)
    if isinstance(data, dict):
        data.setdefault("id", slideshow_id)
    return data


@router.post("/slideshow-videos", status_code=status.HTTP_202_ACCEPTED)
async def create_slideshow_videos(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    validate_body(payload, settings.SLIDESHOW_SCHEMAS_PATH / "SlideshowVideoCreate.json")
    example = _maybe_example("slideshow-videos.create", settings.SLIDESHOW_EXAMPLES_PATH)
    if example is not None:
        return example
    return _response_from_schema("SlideshowVideoJob.json", settings)


@router.get("/slideshow-videos/{video_id}")
async def get_slideshow_video(video_id: str, settings: Settings = Depends(get_settings)) -> Any:
    data = _response_from_schema("SlideshowVideoJob.json", settings)
    if isinstance(data, dict):
        data.setdefault("id", video_id)
        data.setdefault("status", "succeeded")
    return data


@router.get("/events")
async def get_events() -> Any:
    return {"events": []}


@router.get("/jobs/{job_id}/logs")
async def get_job_logs(job_id: str) -> Any:
    return {"lines": []}


# Voices and Assets minimal support
@router.get("/voices")
async def list_voices() -> Any:
    return []


@router.post("/voices", status_code=status.HTTP_201_CREATED)
async def create_voice(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    validate_body(payload, settings.SLIDESHOW_SCHEMAS_PATH / "VoiceCreate.json")
    data = _response_from_schema("Voice.json", settings)
    return data


@router.post("/assets", status_code=status.HTTP_201_CREATED)
async def create_asset(payload: Dict[str, Any] = Body(...), settings: Settings = Depends(get_settings)) -> Any:
    validate_body(payload, settings.SLIDESHOW_SCHEMAS_PATH / "AssetCreate.json")
    return _response_from_schema("Asset.json", settings)


@router.get("/assets/{asset_id}")
async def get_asset(asset_id: str, settings: Settings = Depends(get_settings)) -> Any:
    data = _response_from_schema("Asset.json", settings)
    if isinstance(data, dict):
        data.setdefault("id", asset_id)
    return data
