from fastapi import FastAPI

app = FastAPI(title="LLM Cost Autopilot")


@app.get("/")
def home():
    return {"message": "LLM Cost Autopilot is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}