from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import HTTPException
from jsonschema import validate as jsonschema_validate
from jsonschema.exceptions import ValidationError


def load_schema(schema_path: Path) -> Any:
    with schema_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_body(instance: Any, schema_path: Path) -> None:
    schema = load_schema(schema_path)
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

