from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "LLM Cost Autopilot is running"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_route():
    fake_result = {
        "text": "Paris.",
        "input_tokens": 10,
        "output_tokens": 5
    }

    with patch("app.main.generate_response", return_value=fake_result):
        with patch("app.main.save_request") as mock_save:
            response = client.post(
                "/route",
                json={"prompt": "What is the capital of France?"}
            )

    assert response.status_code == 200

    data = response.json()

    assert data["selected_model"] == "gpt-6-luna"
    assert data["response"] == "Paris."
    assert data["input_tokens"] == 10
    assert data["output_tokens"] == 5

    mock_save.assert_called_once()
    