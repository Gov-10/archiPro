from fastapi import FastAPI
can_app = FastAPI()

@can_app.get("/")
def hello():
    return {"hello" : "guys"}
