from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.api.routes import chat, files, profile, tasks
from app.db.database import Base, engine


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Peak Haunt API", lifespan=lifespan)

app.include_router(chat.router, prefix="/api/v1", tags=["chat"])
app.include_router(files.router, prefix="/api/v1", tags=["files"])
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
app.include_router(profile.router, prefix="/api/v1", tags=["profile"])

@app.get("/")
def read_root():
    return {"message": "Peak Haunt API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
