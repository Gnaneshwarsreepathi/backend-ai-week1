from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello from FlyRank Backend AI Internship!"
    }

@app.get("/about")
def about():
    return {
        "name": "Sreepathi Gnaneshwar",
        "track": "Backend AI Engineering",
        "week": 1
    }