from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.endpoints import router
from src.db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    pass


app = FastAPI(
    title="Material Cost Calculator",
    lifespan=lifespan
)

app.include_router(router)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}