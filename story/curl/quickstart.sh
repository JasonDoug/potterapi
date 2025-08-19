
#!/bin/bash
# Create a video job
curl -X POST http://localhost:8000/v1/videos \
  -H "Content-Type: application/json" \
  -d @examples/video-create.json

# Create a storyboard
curl -X POST http://localhost:8000/v1/storyboards \
  -H "Content-Type: application/json" \
  -d @examples/storyboard-create.json

# Create a story (end-to-end)
curl -X POST http://localhost:8000/v1/stories \
  -H "Content-Type: application/json" \
  -d @examples/story-create.json
