MODEL_PRICES = {
    "gpt-6-luna": {
        "input": 0.10,
        "output": 0.50
    },
    "gpt-6.1-sol": {
        "input": 2.00,
        "output": 10.00
    }
}


def calculate_cost(model: str, input_tokens: int, output_tokens: int):
    prices = MODEL_PRICES[model]

    input_cost = (input_tokens / 1_000_000) * prices["input"]
    output_cost = (output_tokens / 1_000_000) * prices["output"]

    return input_cost + output_cost