from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello World"}

@app.get("/item")
def get_item(id: int):
    time.sleep(0.1)  # Simulate database work
    return {"id": id}

@app.post("/login")
def login(data: dict):
    time.sleep(0.2)  # Simulate authentication
    return {"status": "success"}