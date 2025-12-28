from fastapi import FastAPI
age_app = FastAPI()

@age_app.get("/")
def hello():
    return {"hello" : "folks"}
