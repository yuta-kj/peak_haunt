from fastapi import FastAPI
from app.api.routes import chat, files, tasks

app = FastAPI(title="Peak Haunt API")

app.include_router(chat.router, prefix="/api/v1", tags=["chat"])
app.include_router(files.router, prefix="/api/v1", tags=["files"])
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Peak Haunt API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
