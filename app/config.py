from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    REPO_ROOT: Path = Path(__file__).resolve().parents[1]
    PROVIDERS_EXAMPLES_PATH: Path = REPO_ROOT / "providers" / "examples"
    SLIDESHOW_SCHEMAS_PATH: Path = REPO_ROOT / "slideshow" / "schemas"
    SLIDESHOW_EXAMPLES_PATH: Path = REPO_ROOT / "slideshow" / "examples"
    STORY_OPENAPI_FILE: Path = REPO_ROOT / "story" / "openapi-video-story.patch.yaml"
    STORY_EXAMPLES_PATH: Path = REPO_ROOT / "story" / "examples"


@lru_cache
def get_settings() -> Settings:
    return Settings()
