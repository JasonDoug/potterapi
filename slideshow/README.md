# Slideshow Media API (Standalone)

This spec defines a standalone pipeline to create slideshow-style videos with narration and music.

**Workflow**: `/scripts` → `/beats` → `/images` → `/voiceovers` → `/background-music` → `/slideshow-videos`

- All POSTs that create work require `Idempotency-Key`.
- Jobs are async; poll GET or use `/v1/events` (SSE) for updates.
- Artifacts are returned as URLs (serve from your CDN).
- Timing sync: prefer `timing_strategy.mode="fit-voiceover"` in `/slideshows` when a voiceover exists.

See `examples/curl-quickstart.sh` for runnable requests.


# Slideshow Media API — Starter Pack

This pack is a ready-to-run foundation for the slideshow pipeline.

## Contents
- `openapi-slideshow.yaml` — OpenAPI 3.1 spec
- `schemas/` — JSON Schemas split from OpenAPI
- `examples/` — canonical request bodies for POST endpoints
- `curl/quickstart.sh` — end-to-end flow (scripts → beats → images → voiceover → bgm → final video)
- `curl/providers.sh` — providers/capabilities/presets demos
- `Postman_Collection.json` + `Postman_Env.json` — import into Postman for quick testing

## Quickstart (curl)
```bash
cd slideshow-pack
export BASE=https://api.example.com
bash curl/quickstart.sh
```

## Notes
- Provide a real `Idempotency-Key` per POST (Postman env has a placeholder).
- All creation endpoints are async; poll GETs or subscribe to `/v1/events` (SSE) in your app.
- Prefer `timing_strategy.mode="fit-voiceover"` once a voiceover exists for best sync.
- Use `presets` to standardize creative defaults per provider (reproducibility).

## Roadmap
- Add `/v1/events` example client
- Add auth examples (API key header and scopes)
- Add cost/usage fields once billing is defined
