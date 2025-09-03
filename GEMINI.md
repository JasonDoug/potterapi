# Project Overview

This project is a FastAPI-based API for Potterlabs, a platform for AI-powered media generation. The API is designed with a layered architecture, providing low-level primitives for direct media manipulation and high-level abstractions for orchestrating complex workflows.

The API is divided into four main subgroups:

*   **Providers:** A registry for managing AI content providers and their capabilities.
*   **Slideshow:** A suite of tools for creating slideshow-style videos with narration and music.
*   **Story:** A set of endpoints for generating videos from scripts, storyboards, and individual video clips.
*   **Video:** A low-level endpoint for direct, provider-agnostic video rendering.

The API is defined using the OpenAPI specification, with a unified mock server that references the individual specs for each subgroup. The project also includes a FastAPI server for running the API, as well as various tools for testing and development.

# Building and Running

To build and run the project, you will need to have Python and Node.js installed.

1.  **Install dependencies:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    npm install
    ```

2.  **Run the FastAPI server:**

    ```bash
    uvicorn app.main:app --reload --port 4009
    ```

3.  **Run the mock server:**

    ```bash
    # For the providers API
    prism mock providers/openapi-providers.yaml --port 4009

    # For the slideshow API
    prism mock slideshow/openapi-slideshow.yaml --port 4010
    ```

# Development Conventions

*   **Coding Style:**
    *   OpenAPI/JSON: 2-space indent; no trailing commas.
    *   Names: snake_case properties; kebab-case path segments; plural resources.
    *   IDs: short prefix + token (e.g., `ss_9`, `vo_7`).
    *   Headers: `Idempotency-Key` required on POSTs.
*   **Testing:**
    *   The server returns example payloads from the `examples/` directory when present; otherwise, it returns stubs from the `schemas/` directory.
    *   Request bodies are validated against JSON Schemas (422 on failure).
    *   Prism is used to verify contracts; schemas and examples should be kept in sync.
*   **Commits and Pull Requests:**
    *   Commits should be imperative and in the present tense.
    *   Pull requests should include a scope summary, impacted endpoints, example payloads, and curl outputs. Any breaking changes should be noted, and notes/collections should be updated when paths or components change.
*   **Security:**
    *   Never commit secrets; prefer environment variables.
    *   Treat artifact URLs as untrusted; use signed/expiring links.

# API Subgroups

## Providers

The Providers API is a registry for managing AI content providers and their capabilities. It provides endpoints for listing providers, getting provider details, and listing provider capabilities.

## Slideshow

The Slideshow API is a suite of tools for creating slideshow-style videos with narration and music. It provides a workflow for creating scripts, generating voiceovers, creating image slideshows, and composing the final video.

## Story

The Story API is a set of endpoints for generating videos from scripts, storyboards, and individual video clips. It provides a high-level abstraction for orchestrating the video creation process.

## Video

The Video API is a low-level endpoint for direct, provider-agnostic video rendering. It provides a simple interface for creating video rendering jobs and checking their status.