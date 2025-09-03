from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def _read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _maybe_example(name: str, examples_path: Path) -> Dict[str, Any] | None:
    p = examples_path / f"{name}.response.json"
    if p.exists():
        return _read_json(p)
    return None
