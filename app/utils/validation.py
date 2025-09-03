from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from fastapi import HTTPException
from jsonschema import validate as jsonschema_validate
from jsonschema.exceptions import ValidationError


def load_schema(schema_path: Path) -> Any:
    with schema_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_schema_from_openapi(openapi_path: Path, schema_name: str) -> Any:
    with openapi_path.open("r", encoding="utf-8") as f:
        openapi_spec = yaml.safe_load(f)
    return openapi_spec["components"]["schemas"][schema_name]


def validate_body(instance: Any, schema: Any) -> None:
    try:
        jsonschema_validate(instance=instance, schema=schema)
    except ValidationError as exc:
        detail = {
            "error": "unprocessable_entity",
            "message": exc.message,
            "path": list(exc.path),
            "schema_path": list(exc.schema_path),
        }
        raise HTTPException(status_code=422, detail=detail) from exc