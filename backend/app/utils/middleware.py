from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000",
    "http://localhost",
    "http://localhost:5500",
    "http://localhost:8000",
]


def setup_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
