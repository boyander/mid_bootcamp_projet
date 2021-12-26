from fastapi import FAstAPI
from .routers import eurocopa

app = FAstAPI()

app.include_router(eurocopa.router)