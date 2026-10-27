from fastapi import FastAPI
from pydantic import BaseModel

from app.router import calculate_complexity, select_model

app = FastAPI(title="LLM Cost Autopilot")

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "LLM Cost Autopilot is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/route")
def route_prompt(request: PromptRequest):
    score = calculate_complexity(request.prompt)
    model = select_model(request.prompt)


    return {
        "prompt" : request.prompt,
        "complexity_score": score,
        "selected_model": model
    }
