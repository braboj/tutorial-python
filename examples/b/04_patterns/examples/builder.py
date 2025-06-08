# Example: Builder Pattern

from abc import ABC, abstractmethod


class Pizza(object):

    def __init__(self):
        self.crust = None
        self.cheese = None
        self.toppings = []

    def __str__(self):
        return "Crust: {0}\nCheese: {1}\nToppings: {2}".format(
            self.crust,
            self.cheese,
            ", ".join(self.toppings)
        )


class PizzaBuilderAbc(ABC):

    @abstractmethod
    def set_crust(self, crust):
        pass

    @abstractmethod
    def add_cheese(self, cheese):
        pass

    @abstractmethod
    def add_topping(self, topping):
        pass

    @abstractmethod
    def build(self):
        pass


class MyPizzaBuilder(object):

    def __init__(self):
        self.pizza = Pizza()

    def set_crust(self, crust):
        self.pizza.crust = crust
        return self

    def add_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def build(self):
        return self.pizza


pizza = (
    MyPizzaBuilder()
    .set_crust("thin")
    .add_cheese("mozzarella")
    .add_topping("pepperoni")
    .add_topping("mushrooms")
    .build()
)

print(pizza)
