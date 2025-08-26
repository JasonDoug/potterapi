#!/usr/bin/env bash
set -euo pipefail

# Unified Prism mock for Providers + Slideshow (Story TBD)
# Usage:
#   bash mock-unified.sh                 # default port 4010, examples-first
#   PORT=5050 bash mock-unified.sh       # custom port
#   MODE=dynamic bash mock-unified.sh    # schema-dynamic responses

PORT=${PORT:-4010}
MODE=${MODE:-examples} # 'examples' (default) or 'dynamic'
SPEC="$(dirname "$0")/openapi-potterlabs.yaml"

if ! command -v prism >/dev/null 2>&1; then
  echo "Prism CLI not found."
  echo "Install globally: npm i -g @stoplight/prism-cli"
  echo "Or run with npx: npx @stoplight/prism-cli@latest mock \"$SPEC\" --port $PORT --cors"
  exit 1
fi

echo "Starting Unified Prism mock on http://localhost:$PORT"
echo "Spec: $SPEC"
echo "Mode: $MODE (examples=prefer embedded examples; dynamic=generate)"
echo "Press Ctrl+C to stop."

if [[ "$MODE" == "dynamic" ]]; then
  exec prism mock "$SPEC" --port "$PORT" --cors --dynamic
else
  exec prism mock "$SPEC" --port "$PORT" --cors
fi

