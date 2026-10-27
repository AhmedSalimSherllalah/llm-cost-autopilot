from fastapi import FastAPI
from pydantic import BaseModel

from app.router import calculate_complexity, select_model
from app.llm import generate_response

from app.cost import calculate_cost


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

    result = generate_response(request.prompt, model)

    cost = calculate_cost(
        model,
        result["input_tokens"],
        result["output_tokens"]
    )

    return {
        "prompt": request.prompt,
        "complexity_score": score,
        "selected_model": model,
        "response": result["text"],
        "input_tokens": result["input_tokens"],
        "output_tokens": result["output_tokens"],
        "cost_usd": cost
    }