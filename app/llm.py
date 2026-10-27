import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_response(prompt: str, model: str):
    response = client.responses.create(
        model=model,
        input=prompt
    )

    return {
        "text": response.output_text,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens
    }