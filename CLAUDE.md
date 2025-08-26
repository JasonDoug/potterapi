# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### FastAPI Server
```bash
# Install dependencies
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

# Run FastAPI server
uvicorn app.main:app --reload --port 4009

# Health check
curl http://localhost:4009/health

# Test providers endpoint
curl http://localhost:4009/providers | jq .

# Test slideshow endpoint (requires Idempotency-Key)
curl -X POST http://localhost:4009/v1/images \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: 00000000-0000-0000-0000-000000000000" \
  -d @slideshow/examples/images.create.json | jq .
```

### Mock Servers (Prism)
```bash
# Install prism globally: npm i -g @stoplight/prism-cli

# Run unified mock (all APIs)
bash mock-unified.sh  # Default port 4010
PORT=5050 bash mock-unified.sh  # Custom port
MODE=dynamic bash mock-unified.sh  # Schema-dynamic responses

# Run individual mocks
bash providers/mock.sh  # Port 4009
bash slideshow/mock.sh  # Port 4010
```

## Architecture Overview

This is a multi-spec OpenAPI project with three main API groups:

### 1. Providers API (`/providers`)
- **Purpose**: Registry of AI content providers and their capabilities
- **Location**: `providers/` directory
- **Endpoints**: `/providers`, `/providers/{id}`, `/providers/{id}/capabilities`
- **Implementation**: FastAPI router at `app/routers/providers.py`
- **Data**: Static JSON files in `providers/examples/`

### 2. Slideshow API (`/v1/*`)
- **Purpose**: Pipeline for creating slideshow-style videos with narration and music
- **Location**: `slideshow/` directory  
- **Workflow**: scripts → beats → images → voiceovers → background-music → slideshow-videos
- **Implementation**: FastAPI router at `app/routers/slideshow.py`
- **Key Feature**: All POST requests require `Idempotency-Key` header

### 3. Story API (Patch - `/videos`, `/storyboards`, `/stories`)
- **Purpose**: Video creation with structured scenes and rendering
- **Location**: `story/` directory
- **Status**: Patch spec, not yet integrated into main server

### Unified Structure
- **Main Spec**: `openapi-potterlabs.yaml` references all sub-specs via `$ref`
- **FastAPI App**: `app/main.py` creates unified server with health check
- **Validation**: JSON Schema validation for all POST request bodies
- **Response Strategy**: Returns examples from `examples/` directories when available, otherwise generates stubs from `schemas/`

## Key Implementation Details

### Schema-Driven Development
- Each API group has its own `schemas/` directory with JSON Schema files
- Request validation uses `app/utils/validation.py`
- Response generation uses `app/utils/stubgen.py` for schema-based stubs
- Examples in `examples/` directories take precedence over generated responses

### ID Conventions
- Short prefixes with tokens: `ss_9` (slideshow), `vo_7` (voiceover), `scr_1` (script)
- Consistent across all APIs for easy identification

### Async Job Pattern
- Most slideshow creation endpoints return 202 Accepted for async processing
- Jobs have status fields (`pending`, `processing`, `succeeded`, `failed`)
- Polling via GET endpoints to check job status

### Middleware
- `Idempotency-Key` validation middleware warns on missing header for POSTs
- JSON Schema validation hook (placeholder for route-specific schemas)

## Testing & Development Workflow

1. **Start Development**: Use FastAPI server for active development with hot reload
2. **API Testing**: Use Prism mocks for contract testing and frontend development  
3. **Request Testing**: Postman collections available in each API directory
4. **Quick Testing**: curl scripts in `slideshow/curl-quickstart.sh` and similar

## File Organization Patterns

```
├── app/                          # FastAPI implementation
│   ├── main.py                   # Server entry point
│   ├── routers/                  # API route handlers
│   └── utils/                    # Validation and stub generation
├── providers/                    # Providers API spec and assets
├── slideshow/                    # Slideshow API spec and assets  
├── story/                        # Story API patch spec
├── openapi-*.yaml               # Main spec files
└── mock-unified.sh              # Unified mock server script
```

Each API directory contains:
- `openapi-*.yaml` - OpenAPI specification
- `schemas/` - JSON Schema files
- `examples/` - Example request/response payloads
- `README.md` - API-specific documentation
- Postman collections and environments