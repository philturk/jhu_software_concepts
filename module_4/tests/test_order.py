##  Unit tests for Order class in order.py

import pytest
from src.order import Order

## Test cases for Order class
## Tests initialization, string representation, pizza input, and payment status              
@pytest.mark.order
def test_order_init():
    order = Order()
    assert isinstance(order.pizzas, list)
    assert order.cost == 0
    assert order.paid is False

## Test string representation of Order object
## Checks if the string contains expected details after adding a pizza
@pytest.mark.order
def test_order_str():
    order = Order()
    order.input_pizza("thin", ["marinara"], "mozzarella", ["pineapple"])
    desc = str(order)
    assert "Customer Requested:" in desc
    assert "thin" in desc
    assert "marinara" in desc
    assert "pineapple" in desc
    assert "Total Cost:" in desc

## Test inputting pizza details into the order
## Checks if cost is updated after adding a pizza 
@pytest.mark.order
def test_order_input_pizza():
    order = Order()
    order.input_pizza("thick", ["pesto"], "mozzarella", ["mushrooms"])
    assert order.cost > 0

## Test marking the order as paid
## Checks if the paid attribute is set to True
@pytest.mark.order
def test_order_paid():
    order = Order()
    order.order_paid()
    assert order.paid is True
