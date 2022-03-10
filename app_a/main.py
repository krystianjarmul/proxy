from fastapi import FastAPI

app = FastAPI()


@app.get("/app_a/sessions")
def list_sessions():
    return "Sessions from app A"
