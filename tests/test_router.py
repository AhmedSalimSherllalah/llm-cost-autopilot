from app.router import calculate_complexity, select_model


def test_simple_prompt():
    prompt = "What is the capital of France?"

    assert calculate_complexity(prompt) == 0
    assert select_model(prompt) == "gpt-6-luna"


def test_complex_prompt():
    prompt = "Compare and explain this algorithm: binary search."

    assert calculate_complexity(prompt) == 3
    assert select_model(prompt) == "gpt-6.1-sol"