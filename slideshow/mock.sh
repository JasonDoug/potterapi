#!/usr/bin/env bash
set -euo pipefail

# Prism mock starter for Slideshow API
# Usage:
#   bash slideshow/mock.sh            # default port 4010, examples mode
#   PORT=5051 bash slideshow/mock.sh  # custom port
#   MODE=dynamic bash slideshow/mock.sh  # enable schema-dynamic responses

PORT=${PORT:-4010}
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPEC="$DIR/openapi-slideshow.yaml"
MODE=${MODE:-examples} # 'examples' (default) or 'dynamic'

if ! command -v prism >/dev/null 2>&1; then
  echo "Prism CLI not found."
  echo "Install globally: npm i -g @stoplight/prism-cli"
  echo "Or run once with npx: npx @stoplight/prism-cli@latest mock \"$SPEC\" --port $PORT --cors"
  exit 1
fi

echo "Starting Prism mock for Slideshow API on http://localhost:$PORT"
echo "Spec: $SPEC"
echo "Mode: $MODE (examples=prefer embedded examples; dynamic=generate)"
echo "Press Ctrl+C to stop."

if [[ "$MODE" == "dynamic" ]]; then
  exec prism mock "$SPEC" --port "$PORT" --cors --dynamic
else
  exec prism mock "$SPEC" --port "$PORT" --cors
fi

