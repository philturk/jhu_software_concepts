## Unit tests for the Pizza class in pizza.py

import pytest
from src.pizza import Pizza

## Test cases for Pizza class
## Tests initialization, string representation, and cost calculation
@pytest.mark.pizza
def test_pizza_init():
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["pineapple"])
    assert pizza.crust == "thin"
    assert isinstance(pizza.sauce, list)
    assert "marinara" in pizza.sauce
    assert pizza.cheese == "mozzarella"
    assert isinstance(pizza.toppings, list)
    assert "pineapple" in pizza.toppings
    assert pizza.cost() > 0

## Test string representation of Pizza object
## Checks if the string contains expected details
@pytest.mark.pizza
def test_pizza_str():
    pizza = Pizza("thick", ["pesto"], "mozzarella", ["mushrooms"])
    desc = str(pizza)
    assert "thick" in desc
    assert "pesto" in desc
    assert "mozzarella" in desc
    assert "mushrooms" in desc
    assert "Cost:" in desc

## Test cost calculation of Pizza object
## Checks if the cost method returns the expected value
## N.b., would be ideal candidate for parameterization to 
## verify multiple combos but was not asked for in homework
@pytest.mark.pizza
def test_pizza_cost():
    pizza = Pizza("thin", ["pesto"], "mozzarella", ["mushrooms"])
    expected_cost = 5 + 3 + 3  # thin crust + pesto + mushrooms
    assert pizza.cost() == expected_cost
