
from app.router import calculate_complexity, select_model

simple_topics = [
    "the capital of France",
    "the capital of Japan",
    "the boiling point of water",
    "the largest ocean",
    "the author of Hamlet",
    "the square root of 64",
    "the meaning of CPU",
    "the meaning of HTML",
    "the number of days in a week",
    "the currency of Japan",
    "the chemical symbol for gold",
    "the freezing point of water",
    "the largest planet",
    "the speed of light",
    "the capital of Italy",
    "the meaning of RAM",
    "the number of continents",
    "the author of 1984",
    "the capital of Spain",
    "the meaning of API",
    "the smallest prime number",
    "the capital of Germany",
    "the formula for water",
    "the number of sides on a hexagon",
    "the capital of Canada",
    "the meaning of SQL",
    "the largest mammal",
    "the capital of Brazil",
    "the number of hours in a day",
    "the meaning of URL",
    "the capital of Australia",
    "the square root of 81",
    "the chemical symbol for oxygen",
    "the number of minutes in an hour",
    "the capital of Egypt",
    "the meaning of GPU",
    "the capital of India",
    "the number of seconds in a minute",
    "the largest desert",
    "the meaning of JSON",
    "the capital of Portugal",
    "the number of months in a year",
    "the chemical symbol for iron",
    "the capital of Greece",
    "the meaning of HTTP",
    "the number of legs on a spider",
    "the capital of Norway",
    "the meaning of DNS",
    "the capital of Sweden",
    "the number of degrees in a circle"
]

complex_topics = [
    "sorting algorithms",
    "database normalization",
    "distributed systems",
    "machine learning models",
    "neural network architectures",
    "REST API security",
    "microservice architectures",
    "database indexing strategies",
    "cloud computing platforms",
    "operating system scheduling",
    "concurrency in Python",
    "SQL query optimization",
    "network routing protocols",
    "cryptographic algorithms",
    "software design patterns",
    "object-oriented programming principles",
    "graph traversal algorithms",
    "dynamic programming",
    "computer memory management",
    "database transaction isolation",
    "authentication protocols",
    "container orchestration",
    "load balancing strategies",
    "software testing methodologies",
    "compiler optimization",
    "data structure performance",
    "event-driven architectures",
    "API rate limiting",
    "distributed database consistency",
    "caching strategies",
    "fault-tolerant systems",
    "asynchronous programming",
    "memory allocation algorithms",
    "database sharding",
    "software architecture tradeoffs",
    "network security vulnerabilities",
    "algorithmic time complexity",
    "message queue architectures",
    "data encryption techniques",
    "CI/CD pipeline design",
    "thread synchronization",
    "database replication",
    "system scalability",
    "cloud infrastructure security",
    "API gateway architectures",
    "graph database performance",
    "distributed consensus algorithms",
    "software dependency management",
    "database deadlock prevention",
    "parallel computing techniques"
]

tests = []

for topic in simple_topics:
    tests.append((f"What is {topic}?", "simple"))

for topic in complex_topics:
    tests.append((f"Compare and analyze {topic} in detail.", "complex"))

correct = 0
luna_count = 0
sol_count = 0

for prompt, expected in tests:
    score = calculate_complexity(prompt)
    model = select_model(prompt)

    predicted = "simple" if model == "gpt-6-luna" else "complex"

    if predicted == expected:
        correct += 1

    if model == "gpt-6-luna":
        luna_count += 1
    else:
        sol_count += 1

    if predicted != expected:
        print(f"Incorrect: {prompt}")
        print(f"Expected: {expected}, Predicted: {predicted}")



print("\n--- BENCHMARK RESULTS ---")
print("Total prompts:", len(tests))
print("Correct classifications:", correct)
print("Accuracy:", round(correct / len(tests) * 100, 2), "%")
print("Luna requests:", luna_count)
print("Sol requests:", sol_count)




print("\n--- REALISTIC ROUTING TEST ---")

realistic_tests = [
    ("Explain what Python is.", "simple"),
    ("Compare cats and dogs.", "simple"),
    ("What is the difference between RAM and ROM?", "simple"),
    ("Debug this distributed payment system.", "complex"),
    ("Design a fault-tolerant payment processing system.", "complex"),
    ("Prove that this algorithm is correct.", "complex"),
    ("What is 25 multiplied by 4?", "simple"),
    ("Explain why distributed databases can become inconsistent.", "complex"),
    ("Write a scalable authentication service.", "complex"),
    ("Summarize this sentence.", "simple")
]

correct = 0

for prompt, expected in realistic_tests:
    model = select_model(prompt)
    predicted = "complex" if model == "gpt-6.1-sol" else "simple"

    if predicted == expected:
        correct += 1

    print(f"{predicted.upper():7} | Expected: {expected:7} | {prompt}")

print(f"\nRealistic accuracy: {correct}/{len(realistic_tests)}")

