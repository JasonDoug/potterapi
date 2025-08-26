from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from fastapi import APIRouter, Body, status

from ..utils.validation import validate_body, load_schema
from ..utils.stubgen import generate_stub


router = APIRouter(prefix="/v1", tags=["Slideshow"])

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMAS_DIR = REPO_ROOT / "slideshow" / "schemas"
EXAMPLES_DIR = REPO_ROOT / "slideshow" / "examples"


def _read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _response_from_schema(schema_file: str) -> Any:
    schema = load_schema(SCHEMAS_DIR / schema_file)
    return generate_stub(schema)


def _maybe_example(name: str) -> Dict[str, Any] | None:
    # Reserved to support future response examples; request examples exist today.
    # If a corresponding "<name>.response.json" exists, return it.
    p = EXAMPLES_DIR / f"{name}.response.json"
    if p.exists():
        return _read_json(p)
    return None


@router.post("/scripts", status_code=status.HTTP_201_CREATED)
async def create_script(payload: Dict[str, Any] = Body(...)) -> Any:
    validate_body(payload, SCHEMAS_DIR / "ScriptCreate.json")
    example = _maybe_example("scripts.create")
    if example is not None:
        return example
    return _response_from_schema("Script.json")


@router.get("/scripts")
async def list_scripts() -> Any:
    # Minimal list stub conforms to ListResponseScripts
    return {"items": []}


@router.get("/scripts/{script_id}")
async def get_script(script_id: str) -> Any:
    data = _response_from_schema("Script.json")
    if isinstance(data, dict):
        data.setdefault("id", script_id)
        data.setdefault("status", "succeeded")
        data.setdefault("created_at", "1970-01-01T00:00:00Z")
        data.setdefault("sections", [])
    return data


@router.post("/beats", status_code=status.HTTP_201_CREATED)
async def create_beats(payload: Dict[str, Any] = Body(...)) -> Any:
    validate_body(payload, SCHEMAS_DIR / "BeatsCreate.json")
    example = _maybe_example("beats.create")
    if example is not None:
        return example
    return _response_from_schema("Beats.json")


@router.get("/beats")
async def list_beats() -> Any:
    # No explicit list schema; return empty for now
    return {"items": []}


@router.post("/images", status_code=status.HTTP_202_ACCEPTED)
async def create_images(payload: Dict[str, Any] = Body(...)) -> Any:
    validate_body(payload, SCHEMAS_DIR / "ImageCreate.json")
    example = _maybe_example("images.create")
    if example is not None:
        return example
    return _response_from_schema("ImageJob.json")


@router.get("/images")
async def list_images() -> Any:
    return {"items": []}


@router.get("/images/{image_job_id}")
async def get_image_job(image_job_id: str) -> Any:
    data = _response_from_schema("ImageJob.json")
    if isinstance(data, dict):
        data.setdefault("id", image_job_id)
        data.setdefault("status", "succeeded")
    return data


@router.post("/voiceovers", status_code=status.HTTP_202_ACCEPTED)
async def create_voiceovers(payload: Dict[str, Any] = Body(...)) -> Any:
    validate_body(payload, SCHEMAS_DIR / "VoiceoverCreate.json")
    example = _maybe_example("voiceovers.create")
    if example is not None:
        return example
    return _response_from_schema("VoiceoverJob.json")


@router.get("/voiceovers")
async def list_voiceovers() -> Any:
    return {"items": []}


@router.get("/voiceovers/{voiceover_id}")
async def get_voiceover(voiceover_id: str) -> Any:
    data = _response_from_schema("VoiceoverJob.json")
    if isinstance(data, dict):
        data.setdefault("id", voiceover_id)
        data.setdefault("status", "succeeded")
    return data


@router.post("/background-music", status_code=status.HTTP_202_ACCEPTED)
async def create_background_music(payload: Dict[str, Any] = Body(...)) -> Any:
    validate_body(payload, SCHEMAS_DIR / "BackgroundMusicCreate.json")
    example = _maybe_example("background-music.create")
    if example is not None:
        return example
    return _response_from_schema("BackgroundMusicJob.json")


@router.get("/background-music/{music_id}")
async def get_background_music(music_id: str) -> Any:
    data = _response_from_schema("BackgroundMusicJob.json")
    if isinstance(data, dict):
        data.setdefault("id", music_id)
        data.setdefault("status", "succeeded")
    return data


@router.post("/slideshows", status_code=status.HTTP_201_CREATED)
async def create_slideshows(payload: Dict[str, Any] = Body(...)) -> Any:
    validate_body(payload, SCHEMAS_DIR / "SlideshowCreate.json")
    example = _maybe_example("slideshows.create")
    if example is not None:
        return example
    return _response_from_schema("Slideshow.json")


@router.get("/slideshows")
async def list_slideshows() -> Any:
    return {"items": []}


@router.get("/slideshows/{slideshow_id}")
async def get_slideshow(slideshow_id: str) -> Any:
    data = _response_from_schema("Slideshow.json")
    if isinstance(data, dict):
        data.setdefault("id", slideshow_id)
    return data


@router.post("/slideshow-videos", status_code=status.HTTP_202_ACCEPTED)
async def create_slideshow_videos(payload: Dict[str, Any] = Body(...)) -> Any:
    validate_body(payload, SCHEMAS_DIR / "SlideshowVideoCreate.json")
    example = _maybe_example("slideshow-videos.create")
    if example is not None:
        return example
    return _response_from_schema("SlideshowVideoJob.json")


@router.get("/slideshow-videos/{video_id}")
async def get_slideshow_video(video_id: str) -> Any:
    data = _response_from_schema("SlideshowVideoJob.json")
    if isinstance(data, dict):
        data.setdefault("id", video_id)
        data.setdefault("status", "succeeded")
    return data


# Voices and Assets minimal support
@router.get("/voices")
async def list_voices() -> Any:
    return []


@router.post("/voices", status_code=status.HTTP_201_CREATED)
async def create_voice(payload: Dict[str, Any] = Body(...)) -> Any:
    validate_body(payload, SCHEMAS_DIR / "VoiceCreate.json")
    data = _response_from_schema("Voice.json")
    return data


@router.post("/assets", status_code=status.HTTP_201_CREATED)
async def create_asset(payload: Dict[str, Any] = Body(...)) -> Any:
    validate_body(payload, SCHEMAS_DIR / "AssetCreate.json")
    return _response_from_schema("Asset.json")


@router.get("/assets/{asset_id}")
async def get_asset(asset_id: str) -> Any:
    data = _response_from_schema("Asset.json")
    if isinstance(data, dict):
        data.setdefault("id", asset_id)
    return data
