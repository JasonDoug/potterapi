# Providers API Pack

This pack defines a standalone API for managing AI content providers and their capabilities.

## Endpoints
- `GET /providers` → List all providers
- `GET /providers/{id}` → Get details for a provider
- `GET /providers/{id}/capabilities` → List capabilities for a provider

## Usage
Run as mock with Prism:
```bash
prism mock openapi-providers.yaml --port 4009
```

Test with curl:
```bash
curl http://localhost:4009/providers
```

Import `postman/Providers.postman_collection.json` into Postman for ready-to-use requests.
