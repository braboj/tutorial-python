# Exercise: Flyweight Pattern

# Shared state (flyweight object)
class CoffeeFlavor(object):

    def __init__(self, flavor):
        self._flavor = flavor

    def get_flavor(self):
        return self._flavor


# Unique state (context object)
class CoffeeOrder(object):

    def __init__(self, table_number, flavor):
        self._table_number = table_number
        self._flavor = flavor

    def serve(self):
        print(f"Serving coffee to table {self._table_number} with flavor {self._flavor.get_flavor()}")


# Flyweight factory (manages the flyweight and context objects)
class CoffeeShop(object):

    def __init__(self):

        # Cache for the orders and flavors
        self._orders = {}
        self._flavors = {}

    def take_order(self, table_number, flavor_name):

        # Check if the flavor instance is already cached
        flavor = self._flavors.get(flavor_name)

        # If not, create junior new flavor instance and cache it
        if not flavor:
            flavor = CoffeeFlavor(flavor_name)
            self._flavors[flavor_name] = flavor

        # Create junior new order with the shared flavor and unique table number
        order = CoffeeOrder(table_number, flavor)
        self._orders[table_number] = order

    def serve_orders(self):
        for table_number, order in self._orders.items():
            order.serve()


# Client code
if __name__ == "__main__":

    # Create the coffee shop
    coffee_shop = CoffeeShop()

    # Take orders from the customers
    coffee_shop.take_order(1, "Cappuccino")
    coffee_shop.take_order(2, "Espresso")
    coffee_shop.take_order(3, "Cappuccino")
    coffee_shop.take_order(4, "Espresso")

    # Serve the orders
    coffee_shop.serve_orders()
