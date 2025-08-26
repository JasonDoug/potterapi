# Repository Guidelines

## Project Structure & Module Organization
- `app/`: FastAPI server (`providers` at root, `slideshow` under `/v1`).
- `providers/`: Registry spec, JSON Schemas, examples, Postman.
- `slideshow/`: Slideshow spec, schemas, examples, curl scripts.
- `story/`: Video/Storyboard/Story patch assets.
- Root specs: `openapi-*.yaml` pointers to packs; `potterlabs-api-bundle/` for merged output.
- Notes: `potterlabs-api-notes.md` summarizes subgroups and tiers.

## Build, Test, and Development Commands
- Install server deps: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
- Run FastAPI: `uvicorn app.main:app --reload --port 4009`
  - Health: `curl http://localhost:4009/health`
  - Providers: `curl http://localhost:4009/providers | jq .`
  - Slideshow (examples): `curl -X POST http://localhost:4009/v1/images -H "Content-Type: application/json" -H "Idempotency-Key: 00000000-0000-0000-0000-000000000000" -d @slideshow/examples/images.create.json | jq .`
- Prism mocks: `bash providers/mock.sh` (PORT=4009, MODE=examples|dynamic), `bash slideshow/mock.sh` (PORT=4010).
- Postman: import collections/envs per pack and set `baseUrl`.

## Coding Style & Naming Conventions
- OpenAPI/JSON: 2‑space indent; no trailing commas.
- Names: snake_case properties; kebab-case path segments; plural resources.
- IDs: short prefix + token (e.g., `ss_9`, `vo_7`).
- Headers: `Idempotency-Key` required on POSTs.

## Testing Guidelines
- Examples first: server returns `examples/` payloads when present; otherwise stubs from `schemas/`.
- Validation: request bodies validated against JSON Schemas (422 on failure).
- Mocks: use Prism to verify contracts; keep schemas and examples in sync.

## Commit & Pull Request Guidelines
- Commits: imperative, present tense (Conventional optional).
- PRs: scope summary, impacted endpoints, example payloads, and curl outputs; note breaking changes; update notes/collections when paths or components change.

## Security & Configuration Tips
- Never commit secrets; prefer env vars.
- Treat artifact URLs as untrusted; use signed/expiring links.
