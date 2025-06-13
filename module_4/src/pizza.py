## Pizza class to represent a pizza order with methods to calculate cost and display details.
## Includes predefined costs for crusts, sauces, and toppings.

class Pizza:
    crust_costs = {
        "thin": 5,
        "thick": 6,
        "gluten_free": 8
    }

    sauce_costs = {
        "marinara": 2,
        "pesto": 3,
        "liv_sauce": 5
    }

    topping_costs = {
        "pineapple": 1,
        "pepperoni": 2,
        "mushrooms": 3
    }

    ##  Method runs automatically when you create a new pizza object.
    def __init__(self, crust, sauce, cheese, toppings):
        if cheese.lower() != "mozzarella":
            raise ValueError("Only mozzarella cheese is allowed.")

        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

    def cost(self):
        total = 0
        total += Pizza.crust_costs.get(self.crust, 0)
        total += sum(Pizza.sauce_costs.get(s, 0) for s in self.sauce)
        total += sum(Pizza.topping_costs.get(t, 0) for t in self.toppings)
        return total

    def __str__(self):
        return (
            f"Crust: {self.crust}, "
            f"Sauce: {self.sauce}, "
            f"Cheese: {self.cheese}, "
            f"Toppings: {self.toppings}, "
            f"Cost: {self.cost()}"
        )
