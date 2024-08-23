from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from .database import Base, engine
from .utils.middleware import setup_middleware
from .utils.routers import include_routers



tags_metadata = [
    {
        "name": "Root",
        "description": "Get the basic info about progect from '/' directory",
    },
    {
        "name": "currency",
        "description": "Operations with currency, get actually currency exchange",
    },
    {
        "name": "convertation",
        "description": "Convert currency by values",
    },
]


# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


# Initialize FastAPI app
def create_app() -> FastAPI:
    app = FastAPI(
        title="Garry's FullStack Project",
        description="## Test API for FullStack project by **(c)Garry**",
        version="0.1-BetaTest",
        contact={
            "name": "Garry",
            "url": "https://github.com/GarryK69",
            "email": "bohdanborejko@proton.me",
        },
        license_info={
            "name": "MIT",
            "url": "https://github.com/GarryK69",
        },
        openapi_url="/api/beta/garry_api.json",
        openapi_tags=tags_metadata,
        lifespan=lifespan,
    )

    # Setup middleware
    setup_middleware(app)

    # Include routers
    include_routers(app)

    # Global error handler
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": f"An unexpected error occurred: {str(exc)}"},
    )

    return app
