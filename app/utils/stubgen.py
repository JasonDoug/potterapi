from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def generate_stub(schema: Dict[str, Any]) -> Any:
    t = schema.get("type")

    if "enum" in schema and isinstance(schema["enum"], list) and schema["enum"]:
        return schema["enum"][0]

    if t == "object" or (t is None and "properties" in schema):
        props = schema.get("properties", {})
        required = set(schema.get("required", []))
        result: Dict[str, Any] = {}
        for name, sub in props.items():
            if name in required:
                result[name] = generate_stub(sub)
        return result

    if t == "array":
        # Return empty list to keep responses lightweight
        return []

    if t == "string":
        fmt = schema.get("format")
        if fmt == "date-time":
            return _now()
        return schema.get("example") or "string"

    if t == "integer":
        return int(schema.get("default", 0))

    if t == "number":
        return float(schema.get("default", 0))

    if t == "boolean":
        return bool(schema.get("default", False))

    # oneOf/anyOf: pick first schema to stub
    for key in ("oneOf", "anyOf", "allOf"):
        if key in schema and isinstance(schema[key], list) and schema[key]:
            return generate_stub(schema[key][0])

    # Fallback
    return {}

