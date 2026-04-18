from fastapi import FastAPI

app = FastAPI(title="Peak Haunt API")

@app.get("/")
def read_root():
    return {"message": "Peak Haunt API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
