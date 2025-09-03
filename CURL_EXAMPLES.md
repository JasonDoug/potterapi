# cURL Examples

This file contains a collection of `curl` commands that you can use to test the Potterlabs API.

## Health Check

```bash
cURL http://localhost:4009/health
```

## Providers

### List Providers

```bash
curl http://localhost:4009/providers | jq .
```

### Get Provider by ID

```bash
curl http://localhost:4009/providers/runway | jq .
```

## Slideshow

### Create a Script

```bash
curl -X POST http://localhost:4009/v1/scripts -H "Content-Type: application/json" -H "Idempotency-Key: 00000000-0000-0000-0000-000000000000" --data '{"input": {"type": "text", "text": "This is a test script."}}' | jq .
```

### Get a Script

```bash
curl http://localhost:4009/v1/scripts/string | jq .
```

## Video

### Create a Video

```bash
curl -X POST http://localhost:4009/v1/videos -H "Content-Type: application/json" -H "Idempotency-Key: 00000000-0000-0000-0000-000000000001" --data '{"provider": "auto", "inputs": {"prompt": "A cat flying in space", "duration_sec": 10}}' | jq .
```

### Get a Video

```bash
curl http://localhost:4009/v1/videos/string | jq .
```

## Story

### Create a Storyboard

```bash
curl -X POST http://localhost:4009/v1/storyboards -H "Content-Type: application/json" -H "Idempotency-Key: 00000000-0000-0000-0000-000000000002" --data '{"script": "This is a test storyboard."}' | jq .
```

### Render a Storyboard

```bash
curl -X POST http://localhost:4009/v1/storyboards/string/render -H "Content-Type: application/json" -H "Idempotency-Key: 00000000-0000-0000-0000-000000000003" --data '{"style": "cinematic"}' | jq .
```

### Create a Story

```bash
curl -X POST http://localhost:4009/v1/stories -H "Content-Type: application/json" -H "Idempotency-Key: 00000000-0000-0000-0000-000000000004" --data '{"title": "My Test Story", "script": "This is a test story."}' | jq .
```

### Get a Story

```bash
curl http://localhost:4009/v1/stories/string | jq .
```
