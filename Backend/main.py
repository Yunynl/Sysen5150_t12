from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SYSEN 5151 Lab 0 assignment"}