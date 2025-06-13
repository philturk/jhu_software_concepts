## Order class for managing pizza orders and overall order details.
## Includes methods for adding pizzas, calculating total cost, and marking as paid.

from src.pizza import Pizza

class Order:
    ## This method sets up the initial state of a new order.
    def __init__(self):
        self.pizzas = []
        self.cost = 0
        self.paid = False

    def __str__(self):
        result = ["Customer Requested:"]
        for pizza in self.pizzas:
            result.append(str(pizza))
        result.append(f"Total Cost: {self.cost}")
        return "\n".join(result)

    def input_pizza(self, crust, sauce, cheese, toppings):
        pizza = Pizza(crust, sauce, cheese, toppings)
        self.pizzas.append(pizza)
        self.cost += pizza.cost()

    def order_paid(self):
        self.paid = True
