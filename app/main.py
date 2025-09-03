import logging
from fastapi import FastAPI, Request
from .routers import providers, slideshow, video, story
from .exceptions import ProviderNotFoundException, provider_not_found_exception_handler


def create_app() -> FastAPI:
    app = FastAPI(
        title="Potterlabs API",
        version="0.1.0",
        description="FastAPI server for Providers and Slideshow groups (work in progress).",
    )

    app.add_exception_handler(ProviderNotFoundException, provider_not_found_exception_handler)

    # Include providers at root to match spec (e.g., /providers)
    app.include_router(providers.router)
    # Slideshow routes under /v1
    app.include_router(slideshow.router)
    app.include_router(video.router)
    app.include_router(story.router)

    @app.get("/health", tags=["Health"])  # simple health check
    async def health():
        return {"ok": True}

    logger = logging.getLogger("potterlabs")
    logging.basicConfig(level=logging.INFO)

    @app.middleware("http")
    async def idempotency_and_validation(request: Request, call_next):
        # Idempotency-Key: warn if missing on POST, but continue
        if request.method.upper() == "POST":
            if "Idempotency-Key" not in request.headers:
                logger.warning("POST %s missing Idempotency-Key header", request.url.path)

            # Placeholder for JSON Schema validation hook by path.
            # When implementing POST routes, call a validator with the appropriate schema.
            # We intentionally don't block here until routes define a schema mapping.

        response = await call_next(request)
        return response

    return app


# Uvicorn entrypoint: `uvicorn app.main:app --reload --port 4009`
app = create_app()
