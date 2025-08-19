# Slideshow Media API — curl quickstart

BASE=https://api.example.com
UUID=$(python - <<'PY'\nimport uuid; print(uuid.uuid4())\nPY)

# 1) Create script
curl -s -X POST $BASE/v1/scripts \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $UUID" \
  -d '{
    "input": { "type": "text", "text": "INTRO...\n\nSECTION 1..." },
    "options": { "normalize": true, "segment": "section" }
  }'

# 2) Detect beats
curl -s -X POST $BASE/v1/beats \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $UUID" \
  -d '{ "script": { "script_id": "scr_1" }, "options": { "granularity": "section" } }'

# 3) Generate images
curl -s -X POST $BASE/v1/images \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $UUID" \
  -d '{
    "provider":"genai",
    "mode":"generate",
    "prompt":"Warm, minimalist illustration, 16:9",
    "count": 4,
    "aspect_ratio":"16:9"
  }'

# 4) Create voiceover
curl -s -X POST $BASE/v1/voiceovers \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $UUID" \
  -d '{
    "script": { "script_id":"scr_1" },
    "voice": { "voice_id":"vx_emma" },
    "options": { "pace":"medium", "format":"wav", "sample_rate_hz":48000, "ssml": true }
  }'

# 5) Build slideshow (auto timing; switch to fit-voiceover to sync)
curl -s -X POST $BASE/v1/slideshows \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $UUID" \
  -d '{
    "beats": { "beats_id":"bt_3" },
    "image_strategy": { "mode":"generate", "provider":"genai", "per_beat":1, "prompt_template":"{beat.summary}, minimalist, 16:9" },
    "caption_strategy": { "source":"beat_summary", "max_chars": 110 },
    "timing_strategy": { "mode":"auto", "per_slide_sec": 4.5 }
  }'

# 6) Generate background music matched to narration and slideshow
curl -s -X POST $BASE/v1/background-music \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $UUID" \
  -d '{ "target": { "voiceover_id":"vo_7", "slideshow_id":"ss_9" }, "options": { "style":"ambient-cinematic", "duration_policy":"fit" } }'

# 7) Compose final slideshow video
curl -s -X POST $BASE/v1/slideshow-videos \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $UUID" \
  -d '{
    "voiceover_id":"vo_7",
    "slideshow_id":"ss_9",
    "music_id":"bgm_2",
    "options": { "transition":"crossfade", "transition_sec":0.5, "resolution":"1080p", "fps":30,
                 "captions":{"mode":"burn-in"}, "ducking":{"enabled":true, "threshold_db":-12} }
  }'
