#!/usr/bin/env bash
set -euo pipefail

BASE=${BASE:-https://api.example.com}
UUID=$(python - <<'PY'\nimport uuid; print(uuid.uuid4())\nPY)

echo "BASE=$BASE"
echo "UUID=$UUID"

# Providers / Capabilities
curl -s "$BASE/v1/providers?kind=image" | jq .
curl -s "$BASE/v1/providers/genai" | jq .
curl -s "$BASE/v1/providers/genai/health" | jq .
curl -s "$BASE/v1/providers/genai/capabilities" | jq .

# Presets
curl -s -X POST "$BASE/v1/presets" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $UUID" \
  -d @examples/presets.create.image.json | jq .
curl -s -X POST "$BASE/v1/presets" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $UUID" \
  -d @examples/presets.create.tts.json | jq .
