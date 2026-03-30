from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Shivanand"}

@app.get("/health")
def health():
    return {"status": "ok"}




"""What just happened? FastAPI creates an ASGI app.
 Uvicorn is the server that actually listens on port 8000 and feeds HTTP requests into your app.
   --reload restarts on file changes — only for dev.

Go to http://localhost:8000/docs — you get a free Swagger UI. 
This alone saves hours of Postman setup.
Senior tip: Always add /health to every app. Docker, Kubernetes, and load balancers
 ping this to check if your app is alive.
"""
#python -m uvicorn 01_setup:app --reload --port 9000