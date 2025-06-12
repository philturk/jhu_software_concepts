## Integration tests cover interactions between Order and Pizza classes
## Focus on scenarios involving multiple pizzas in a single order

import pytest
from src.order import Order

@pytest.mark.order
@pytest.mark.pizza
def test_multiple_pizzas_per_order():
    order = Order()
    order.input_pizza("thin", ["pesto"], "mozzarella", ["mushrooms"])
    order.input_pizza("thick", ["marinara"], "mozzarella", ["mushrooms"])
    expected_cost = (5 + 3 + 3) + (6 + 2 + 3)
    assert len(order.pizzas) == 2
    assert order.cost == expected_cost
