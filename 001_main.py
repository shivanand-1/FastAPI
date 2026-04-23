import fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return "hello shiva"