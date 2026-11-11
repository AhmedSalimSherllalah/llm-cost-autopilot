from app.cost import calculate_cost, calculate_savings
import pytest


def test_luna_cost():
    cost = calculate_cost("gpt-6-luna", 1000, 500)

    assert cost == 0.00035

def test_savings():
    savings = calculate_savings("gpt-6-luna", 1000, 500)

    assert savings == pytest.approx(0.00665)