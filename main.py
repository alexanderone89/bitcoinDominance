from fastapi import FastAPI

from sheduler import lifespan
from router import router as router_crypto


app = FastAPI(lifespan=lifespan)

app.include_router(router_crypto)
