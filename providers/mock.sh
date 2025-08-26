#!/usr/bin/env bash
set -euo pipefail

# Prism mock starter for Providers API
# Usage:
#   bash providers/mock.sh            # default port 4009
#   PORT=5050 bash providers/mock.sh  # custom port

PORT=${PORT:-4009}
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPEC="$DIR/openapi-providers.yaml"

if ! command -v prism >/dev/null 2>&1; then
  echo "Prism CLI not found."
  echo "Install globally: npm i -g @stoplight/prism-cli"
  echo "Or run once with npx: npx @stoplight/prism-cli@latest mock \"$SPEC\" --port $PORT --cors --dynamic"
  exit 1
fi

MODE=${MODE:-examples} # 'examples' (default) or 'dynamic'

echo "Starting Prism mock for Providers API on http://localhost:$PORT"
echo "Spec: $SPEC"
echo "Mode: $MODE (examples=prefer embedded examples; dynamic=generate)"
echo "Press Ctrl+C to stop."

if [[ "$MODE" == "dynamic" ]]; then
  exec prism mock "$SPEC" --port "$PORT" --cors --dynamic
else
  # Static mode: prefer embedded examples for deterministic payloads
  exec prism mock "$SPEC" --port "$PORT" --cors
fi
