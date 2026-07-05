from fastapi import FastAPI
import requests

app = FastAPI()

print("hello")

@app.get("/")
def home():
    return {"status": "ok"}