# Example: Prototype Pattern

from abc import ABC, abstractmethod


class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass


class Pizza(Prototype):

    def __init__(self, crust, cheese, toppings):
        self.crust = crust
        self.cheese = cheese
        self.toppings = toppings

    def __str__(self):
        return "Crust: {0}\nCheese: {1}\nToppings: {2}".format(
            self.crust,
            self.cheese,
            ", ".join(self.toppings)
        )

    def clone(self):
        return Pizza(self.crust, self.cheese, self.toppings)


if __name__ == "__main__":

    pizza = Pizza("thin", "mozzarella", ["pepperoni", "mushrooms"])

    pizza_clone = pizza.clone()
    print(pizza_clone)

    print(pizza == pizza_clone)
    print(pizza is pizza_clone)
