
# Video/Storyboard/Story Patch

This patch adds three subgroups to the existing Providers+Slideshow API:

- **/videos**: low-level provider-agnostic video jobs
- **/storyboards**: structured scenes & rendering
- **/stories**: orchestration endpoint (script → storyboard → video)

## Files
- `openapi-video-story.patch.yaml`: Patch OpenAPI spec
- `examples/`: Example JSON requests
- `curl/quickstart.sh`: Quick test script
- `Postman_Collection.json` + `Postman_Env.json`: Ready to import into Postman

## Usage
1. Run `curl/curl-quickstart.sh` to try out endpoints (adjust base URL).
2. Import Postman collection/environment and set `baseUrl` to your API.

Integrate this spec into your main API by merging the `paths` and `components.schemas` sections.
