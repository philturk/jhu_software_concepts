from src.pizza import Pizza

class Order:
    """
    A class that represents a full customer order, which can contain multiple pizzas.
    """

    def __init__(self):
        """
        Initialize a new empty order with no pizzas and unpaid status.
        """
        self.pizzas = []
        self.cost = 0
        self.paid = False

    def __str__(self):
        """
        Return a string summary of the full order and total cost.

        :return: Human-readable summary of the order.
        :rtype: str
        """
        result = ["Customer Requested:"]
        for pizza in self.pizzas:
            result.append(str(pizza))
        result.append(f"Total Cost: {self.cost}")
        return "\n".join(result)

    def input_pizza(self, crust, sauce, cheese, toppings):
        """
        Add a pizza to the order and update the total cost.

        :param crust: Crust type.
        :type crust: str
        :param sauce: List of sauces.
        :type sauce: list[str]
        :param cheese: Type of cheese (must be mozzarella).
        :type cheese: str
        :param toppings: List of toppings.
        :type toppings: list[str]
        :return: None
        """
        pizza = Pizza(crust, sauce, cheese, toppings)
        self.pizzas.append(pizza)
        self.cost += pizza.cost()

    def order_paid(self):
        """
        Mark the order as paid by setting paid to True.
        """
        self.paid = True
