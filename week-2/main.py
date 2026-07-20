from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Task API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }