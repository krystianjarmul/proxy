from fastapi import FastAPI

app = FastAPI()


@app.get("/app_c/sessions")
def list_sessions():
    return "Sessions from app C"
