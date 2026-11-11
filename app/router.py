
def calculate_complexity(prompt: str):
    score = 0
    prompt_lower = prompt.lower()

    complex_keywords = [
        "analyse", "analyze", "compare", "explain",
        "evaluate", "debug", "algorithm", "reason",
        "design", "prove", "scalable", "distributed",
        "fault-tolerant", "optimize", "architecture"
    ]

    if len(prompt) > 200:
        score += 1

    for keyword in complex_keywords:
        if keyword in prompt_lower:
            score += 1

    return score



def select_model(prompt: str):
    score = calculate_complexity(prompt)

    if score >= 2:
        return "gpt-6.1-sol"

    return "gpt-6-luna"
