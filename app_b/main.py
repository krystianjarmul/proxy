from fastapi import FastAPI

app = FastAPI()


@app.get("/app_b/sessions")
def list_sessions():
    return "Sessions from app B"
