# Design Patterns

## Abstract Factory

```python
# Example: Abstract Factory

from abc import ABC, abstractmethod


class Button(ABC):
    # Abstract interface for buttons

    @abstractmethod
    def paint(self):
        raise NotImplementedError


class WinButton(Button):
    # Concrete foo for Windows buttons

    def paint(self):
        print("WinButton")


class LinuxButton(Button):

    def paint(self):
        print("LinuxButton")


class Menu(ABC):
    # Abstract interface for menus

    @abstractmethod
    def paint(self):
        raise NotImplementedError


class WinMenu(Menu):
    # Concrete foo for Windows menus

    def paint(self):
        print("WindowsMenu")


class LinuxMenu(Menu):
    # Concrete foo for Linux menus

    def paint(self):
        print("LinuxMenu")


class GUIFactory(ABC):

    # Abstract factory that declares a set of methods for creating each of the
    # products. These methods must return abstract foo types represented by
    # the abstract interfaces Button and Menu.

    @abstractmethod
    def create_button(self) -> Button:
        raise NotImplementedError

    @abstractmethod
    def create_menu(self) -> Menu:
        raise NotImplementedError


class WinFactory(GUIFactory):

    # The concrete factory for Windows foo variants.

    def create_button(self):
        return WinButton()

    def create_menu(self):
        return WinMenu()


class LinuxFactory(GUIFactory):

    # The concrete factory for Linux foo variants.

    def create_button(self):
        return LinuxButton()

    def create_menu(self):
        return LinuxMenu()


if __name__ == "__main__":

    os = input("Select OS: ")

    if os == "win":
        factory = WinFactory()

    elif os == "linux":
        factory = LinuxFactory()

    else:
        raise ValueError("Invalid GUI")

    # Create the GUI
    button = factory.create_button()
    menu = factory.create_menu()
    gui = [button, menu]

    # Paint the GUI
    for item in gui:
        item.paint()
```

## Adapter With Composition

```python
# Example: Adapter Pattern (Object Adapter)

class ChannelV1(object):

    @staticmethod
    def applyConfig():
        # method name from actual legacy code in the company
        print('Configuration method of the old device class!')


class ChannelV2(object):

    @staticmethod
    def configure():
        print('Configuration method of the new device class!')


class ChannelAdapter(ChannelV1):
    # Class adapter (with composition)

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def applyConfig(self):
        self.adaptee.configure()


def host_app(channel):
    channel.applyConfig()


if __name__ == "__main__":
    # Original code using the old service
    host_app(channel=ChannelV1())

    # Use adapter for the new service adapted to the old interface
    host_app(channel=ChannelAdapter(adaptee=ChannelV2()))
```

## Adapter With Inheritance

```python
class ChannelV1(object):

    @staticmethod
    def applyConfig():
        # method name from actual legacy code in the company (Python 2.7)
        print('Configuration method of the old device class!')


class ChannelV2(object):

    @staticmethod
    def configure():
        print('Configuration method of the new device class!')


class ChannelAdapter(ChannelV1, ChannelV2):
    # Class adapter (with inheritance)

    def applyConfig(self):
        # The adapter's applyConfig method calls the new class's configure method
        self.configure()


def host_app(channel):
    # The host_app function works with the ChannelV1 interface
    channel.applyConfig()


if __name__ == "__main__":
    # Original code using the old service (ChannelV1)
    host_app(channel=ChannelV1())

    # Use adapter for the new service (ChannelV2) adapted to the old interface (ChannelV1)
    host_app(channel=ChannelAdapter())
```

## Bridge

```python
# Example: Bridge Pattern with shapes and colors

class Color(object):
    # Interface for Implementation

    def __init__(self, name):
        self.name = name

    def paint(self, shape):
        raise NotImplementedError


class Red(Color):
    # Concrete implementation for red color

    def __init__(self):
        super(Red, self).__init__('red')

    def paint(self, shape):
        print('Painting the {} with red color'.format(shape))


class Blue(Color):
    # Concrete implementation for blue color

    def __init__(self):
        super(Blue, self).__init__('blue')

    def paint(self, shape):
        print('Painting the {} with blue color'.format(shape))


class Shape(object):
    # This is the abstaction used by the client

    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    # Refinded abstraction for circles

    def draw(self):
        print('Drawing a circle')
        self.color.paint(shape='circle')


class Square(Shape):
    # Refined abstraction for squares

    def draw(self):
        print('Drawing a square')
        self.color.paint(shape='square')


class DrawApp(object):
    # This is the client class

    @staticmethod
    def draw(shape: Shape):
        shape.draw()


if __name__ == "__main__":

    # Draw a red circle
    app = DrawApp()

    # Draw shapes
    app.draw(shape=Circle(color=Red()))
    app.draw(shape=Square(color=Blue()))
```

## Builder

```python
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
```

## Chain

```python

```

## Chain Of Responsibility

```python
# Example: Chain of Responsibility Pattern

# Handler interface

class Approver(object):
    def __init__(self, successor=None):
        self.successor = successor

    def set_successor(self, successor):
        self.successor = successor

    def approve(self, purchase):
        pass


# Concrete handlers

class TeamLeader(Approver):
    def approve(self, purchase):
        if purchase <= 1000:
            print(f"Team Leader approves the purchase of ${purchase}")
        elif self.successor:
            self.successor.approve(purchase)


class Manager(Approver):
    def approve(self, purchase):
        if 1000 < purchase <= 5000:
            print(f"Manager approves the purchase of ${purchase}")
        elif self.successor:
            self.successor.approve(purchase)


class Director(Approver):
    def approve(self, purchase):
        if 5000 < purchase <= 10000:
            print(f"Director approves the purchase of ${purchase}")
        elif self.successor:
            self.successor.approve(purchase)


class President(Approver):
    def approve(self, purchase):
        if purchase > 10000:
            print(f"President approves the purchase of ${purchase}")
        elif self.successor:
            self.successor.approve(purchase)


# Client code

if __name__ == "__main__":

    # Define the roles in the chain of responsibility
    team_leader = TeamLeader()
    manager = Manager()
    director = Director()
    president = President()

    # Set the successors
    team_leader.set_successor(manager)
    manager.set_successor(director)
    director.set_successor(president)


    # Create purchases
    purchases = [500, 1000, 2000, 5000, 10000, 20000]

    # Process the purchases
    for purchase in purchases:
        team_leader.approve(purchase)
```

## Command

```python
# Example: Command Pattern


# Command interface
class Command(object):
    def execute(self):
        pass

    def undo(self):
        pass


# Concrete commands
class TypeCommand(Command):
    def __init__(self, text, document):
        self.text = text
        self.document = document

    def execute(self):
        self.document.add_text(self.text)

    def undo(self):
        self.document.remove_text(self.text)


# Receiver class
class Document(object):
    def __init__(self):
        self.content = ""

    def add_text(self, text):
        self.content += text

    def remove_text(self, text):
        if text and text in self.content:
            self.content = self.content.replace(text, "", 1)

    def get_content(self):
        return self.content


# Invoker class (TextEditor)
class TextEditor(object):

    def __init__(self):
        self.history = []

    def execute(self, command):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()


# Client code
if __name__ == "__main__":

    document = Document()
    editor = TextEditor()

    print("Initial content:", document.get_content())

    # Type some text
    type_action1 = TypeCommand("Hello, ", document)
    editor.execute(type_action1)
    print("After typing:", document.get_content())

    type_action2 = TypeCommand("world!", document)
    editor.execute(type_action2)
    print("After typing:", document.get_content())

    # Undo the last command
    editor.undo_last_command()
    print("After undo:", document.get_content())
```

## Composite

```python
# Example: Composite pattern

from abc import abstractmethod


class IComponent(object):
    # Interface used by both the leaf and composite classes

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self):
        raise NotImplementedError


class Leaf(IComponent):

    def execute(self):
        return "{} running".format(self.name)


# Concrete implementation of the composite class
class Composite(IComponent):
    # This is the composite class (tree is composed of leafs)

    def __init__(self, name="Root"):
        super(Composite, self).__init__(name)
        self.components = []

    def add(self, c):
        self.components.append(c)
        return self

    def remove(self, c):
        self.components.remove(c)
        return self

    def get_children(self):
        return self.components

    def execute(self):

        # Delegate work to all the children
        for child in self.components:
            print("{} / {}".format(self.name, child.execute()))

        return "{} running".format(self.name)


if __name__ == "__main__":

    # Define composite foo
    product = Composite()
    product.add(Leaf("Leaf 1"))
    product.add(Leaf("Leaf 2"))
    print(product.execute())

    print()

    # Nested composite foo
    product.add(
        Composite("Subsystem A")
        .add(Leaf("Leaf 1"))
        .add(Leaf("Leaf 2"))
    )
    print(product.execute())
```

## Decorator

```python
# Example: Decorator Pattern

from abc import ABC, abstractmethod


class NotifierAbc(ABC):

    @abstractmethod
    def notify(self):
        pass


class Notifier(NotifierAbc):

    def notify(self):
        print("Print on screen ...")


class NotifierDecorator(NotifierAbc):

    def __init__(self, component):
        self._component = component

    @abstractmethod
    def notify(self):
        pass


class EmailNotifier(NotifierDecorator):

    @staticmethod
    def send_email():
        print("Sending email ...")

    def notify(self):
        self.send_email()
        self._component.notify()


class SMSNotifier(NotifierDecorator):

    @staticmethod
    def send_sms():
        print("Sending SMS ...")

    def notify(self):
        self.send_sms()
        self._component.notify()


def main():
    notifier = Notifier()
    notifier_with_email = EmailNotifier(notifier)
    notifier_with_email_and_sms = SMSNotifier(notifier_with_email)
    notifier_with_email_and_sms.notify()


if __name__ == "__main__":
    main()
```

## Facade

```python
# Example: Facade Pattern

class PumpSystem(object):

    @staticmethod
    def prepare():
        print("SubsystemA prepare ...")

    @staticmethod
    def run():
        print("SubsystemA run ...")


class VentilationSystem(object):

    @staticmethod
    def prepare():
        print("SubsystemB prepare ...")

    @staticmethod
    def run():
        print("SubsystemB run ...")


class ComplexSystemFacade(object):

    def __init__(self):
        self._subsystemA = PumpSystem()
        self._subsystemB = VentilationSystem()

    def run(self):
        self._subsystemA.prepare()
        self._subsystemB.prepare()
        self._subsystemA.run()
        self._subsystemB.run()


def main():
    system = ComplexSystemFacade()
    system.run()


if __name__ == "__main__":
    main()
```

## Factory Class Method

```python
# Example: Factory Method as a class method

class Transport(object):
    def __init__(self):
        pass

    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        print("Delivering by land in a box")


class Ship(Transport):
    def deliver(self):
        print("Delivering by sea in a container")


class Logistic(object):
    def __init__(self, transport):
        self.transport = transport

    def deliver(self):
        self.transport.deliver()

    @classmethod
    def from_json(cls, json):
        # Factory method

        # Get transport type
        token = json.get("transport_type")

        # Convert to lowercase and remove whitespace
        transport_type = token.lower().strip(" \t\n\r")

        # Factory logic
        if transport_type == "truck":
            return Truck()

        elif transport_type == "ship":
            return Ship()

        else:
            raise ValueError("Invalid transport type")


class App(object):

    @staticmethod
    def run():

        # Select transport
        json = {"transport_type": "truck"}
        transport = Logistic.from_json(json)

        # Deliver
        logistic = Logistic(transport)
        logistic.deliver()


if __name__ == "__main__":
    app = App()
    app.run()
```

## Factory Static Method

```python
# Example: Factory Method as a static Method

class Transport(object):
    def __init__(self):
        pass

    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        print("Delivering by land in a box")


class Ship(Transport):
    def deliver(self):
        print("Delivering by sea in a container")


class Logistic(object):
    def __init__(self, transport):
        self.transport = transport

    def deliver(self):
        self.transport.deliver()


class App(object):

    @staticmethod
    def select_transport():
        # Factory method

        # Get transport type
        token = input("Select transport type: ")

        # Convert to lowercase and remove whitespace
        transport_type = token.lower().strip(" \t\n\r")

        # Factory logic
        if transport_type == "truck":
            return Truck()

        elif transport_type == "ship":
            return Ship()

        else:
            raise ValueError("Invalid transport type")

    def run(self):

        # Select transport
        transport = self.select_transport()

        # Deliver
        logistic = Logistic(transport)
        logistic.deliver()


if __name__ == "__main__":
    app = App()
    app.run()
```

## Flyweight

```python
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

        # If not, create a new flavor instance and cache it
        if not flavor:
            flavor = CoffeeFlavor(flavor_name)
            self._flavors[flavor_name] = flavor

        # Create a new order with the shared flavor and unique table number
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
```

## Interpreter

```python
# Example: Interpreter Pattern

# Abstract Expression
class Expression(object):

    def interpret(self, context):
        raise NotImplementedError


# Terminal Expression
class Number(Expression):

    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


# Non-terminal Expression
class Add(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


# Context
class Context(object):

    def __init__(self):
        self.variables = {}

    def set(self, variable, value):
        self.variables[variable] = value

    def get(self, variable):
        return self.variables.get(variable, 0)


# Client code
if __name__ == "__main__":

    context = Context()
    context.set("x", 10)
    context.set("y", 5)

    expression = Add(
        Number(context.get("x")),
        Number(context.get("y"))
    )

    result = expression.interpret(context)
    print("Result: {}".format(result))
```

## Iterator

```python
# Example: Iterator Pattern


# Iterator interface
class Iterator(object):
    def has_next(self):
        pass

    def next(self):
        pass


# TreeNode represents a node in a tree
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


# Concrete Iterator for tree traversal
class TreeIterator(Iterator):
    def __init__(self, root):
        self.stack = [root]

    def has_next(self):
        return len(self.stack) > 0

    def next(self):
        if not self.has_next():
            raise StopIteration()

        node = self.stack.pop()
        for child in reversed(node.children):
            self.stack.append(child)
        return node.data


# Client code
if __name__ == "__main__":

    # Create a sample tree structure
    root = TreeNode("Root")
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    child3 = TreeNode("Child 3")

    # Add nodes to the tree
    root.add_child(child1)
    root.add_child(child2)
    child2.add_child(child3)

    # Create a tree iterator
    iterator = TreeIterator(root)

    # Traverse and print tree nodes
    while iterator.has_next():
        node = iterator.next()
        print(node)
```

## Mediator

```python
# Example: Mediator Pattern


# Mediator interface
class Mediator(object):

    def forward(self, message, component):
        raise NotImplementedError


# Concrete Mediator
class Dialog(Mediator):

    def __init__(self):
        self.components = []

    def set_component(self, component):
        self.components.append(component)

    def forward(self, message, sender):
        for component in self.components:
            if sender is not component:
                component.receive(message)


# Component interface
class Component(object):

    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, message):
        raise NotImplementedError

    def receive(self, message):
        raise NotImplementedError


# Concrete Component
class Button(Component):

    def send(self, message):
        print(f"Button sends: {message}")
        self.mediator.forward(message, self)

    def receive(self, message):
        print(f"Button receives: {message}")


# Concrete Component
class Textbox(Component):

    def send(self, message):
        print(f"Textbox sends: {message}")
        self.mediator.forward(message, self)

    def receive(self, message):
        print(f"Textbox receives: {message}")


# Concrete Component
class Checkbox(Component):

    def send(self, message):
        print(f"Checkbox sends: {message}")
        self.mediator.forward(message, self)

    def receive(self, message):
        print(f"Checkbox receives: {message}")


# Client code
if __name__ == "__main__":

    # Create the mediator
    mediator = Dialog()

    # Add components to the mediator
    button = Button(mediator)
    mediator.set_component(button)

    # Add more components to the mediator
    textbox = Textbox(mediator)
    mediator.set_component(textbox)

    # Add more components to the mediator
    checkbox = Checkbox(mediator)
    mediator.set_component(checkbox)

    # Send messages
    button.send("Hello from Button!")
```

## Memento

```python
# Example: Memento Pattern

# Originator class
class TextEditor:
    def __init__(self):
        self.content = ""

    def write(self, text):
        self.content += text

    def show_content(self):
        print(f"Editor Content: {self.content}")

    def create_memento(self):
        return TextEditorMemento(self.content)

    def restore_from_memento(self, memento):
        self.content = memento.get_state()


# Memento class
class TextEditorMemento:
    def __init__(self, content):
        self.content = content

    def get_state(self):
        return self.content


# Caretaker class
class History:
    def __init__(self):
        self.states = []

    def push(self, memento):
        self.states.append(memento)

    def pop(self):
        if self.states:
            return self.states.pop()
        return None


# Client code
if __name__ == "__main__":

    text_editor = TextEditor()
    history = History()

    text_editor.write("Hello, ")
    history.push(text_editor.create_memento())

    text_editor.write("world!")
    history.push(text_editor.create_memento())

    text_editor.show_content()

    text_editor.write(" Hello, hello!")
    text_editor.show_content()

    # Undo the last action
    last_state = history.pop()
    if last_state:
        text_editor.restore_from_memento(last_state)

    text_editor.show_content()
```

## Observer

```python
# Example: Observer Pattern

# Subject Interface (produces data)
class Publisher(object):

    def attach(self, observer):
        pass

    def detach(self, observer):
        pass

    def notify(self):
        pass


# Concrete Subject
class WeatherData(Publisher):

    def __init__(self):
        self.subscribers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def attach(self, observer):
        self.subscribers.append(observer)

    def detach(self, observer):
        self.subscribers.remove(observer)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self.temperature, self.humidity, self.pressure)

    def set(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify()


# Observer interface (consumes data)
class Subscriber(object):

    def update(self, temperature, humidity, pressure):
        pass


# Concrete Observer
class DisplayDevice(Subscriber):

    def __init__(self, name):
        self.name = name

    def update(self, temperature, humidity, pressure):
        print(
            f"{self.name} Display - Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")


# Client code
if __name__ == "__main__":

    # Create a weather station
    weather_station = WeatherData()

    # Attach a display device to the weather station
    display1 = DisplayDevice("Display 1")
    weather_station.attach(display1)

    # Attach another display device to the weather station
    display2 = DisplayDevice("Display 2")
    weather_station.attach(display2)

    # Simulate changes in weather data
    weather_station.set(25.0, 60.0, 1013.0)
    weather_station.set(26.5, 55.0, 1010.5)
```

## Prototype

```python
# Example: Prototype Pattern

from abc import ABC, abstractmethod


# Prototype interface
class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass


# Concrete Prototype
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
```

## Proxy

```python
# Example: Proxy Pattern

class Server(object):

    def request(self):
        raise NotImplementedError


class RealServer(Server):

    def request(self):
        print("RealServer: Handling request.")


class ProxyServer(Server):

    def __init__(self, server: Server = None):
        self._server = server

    def request(self):
        if self.check_access():
            self._server.request()
            self.log_access()

    @staticmethod
    def check_access():
        print("ProxyServer: Checking access prior to firing a real request.")
        return True

    @staticmethod
    def log_access():
        print("ProxyServer: Logging the time of request.", end="")


class Client(object):

    def __init__(self, server: Server):
        self._server = server

    def execute(self):
        self._server.request()


if __name__ == "__main__":

    print("Client: Executing the client code with a real server")
    real_server = RealServer()
    client = Client(server=real_server)
    client.execute()

    print("")

    print("Client: Executing the same client code with a proxy server")
    client = Client(server=ProxyServer(real_server))
    client.execute()
```

## Singleton

```python
# Example: Singleton Pattern with __new__


class Singleton(object):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)

        return cls.__instance


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
```

## State

```python
# State interface
class State(object):

    def connect(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError

    def send_data(self, data):
        raise NotImplementedError


# Concrete State: Disconnected
class DisconnectedState(State):

    def connect(self):

        # Action
        print("Connecting to the server...")

        # Transition to the Connected state
        return ConnectedState()

    def disconnect(self):
        print("Already disconnected.")
        return self

    def send_data(self, data):

        print("Cannot send data while disconnected.")
        return self


# Concrete State: Connected
class ConnectedState(State):

    def connect(self):

        # Action
        print("Already connected.")

        # Transition
        return self

    def disconnect(self):
        # Action
        print("Disconnecting from the server...")

        # Transition
        return DisconnectedState()

    def send_data(self, data):
        # Action
        print(f"Sending data to the server: {data}")

        # Transition
        return self


# Context class
class Client(object):

    def __init__(self):
        # Initial state
        self.state = DisconnectedState()

    def connect(self):
        self.state = self.state.connect()

    def disconnect(self):
        self.state = self.state.disconnect()

    def send_data(self, data):
        self.state.send_data(data)


# Client code
if __name__ == "__main__":

    client = Client()

    client.send_data("Hello, server!")  # Try sending data while disconnected

    client.connect()
    client.send_data("Hello, server!")  # Send data after connecting

    client.connect()  # Try connecting again

    client.disconnect()
    client.send_data("Goodbye, server!")  # Send data after disconnecting
```

## Strategy

```python
# Example: Strategy Pattern

# Strategy interface
class TextFormatter(object):

    def format_text(self, text):
        raise NotImplementedError


# Concrete Strategy: Uppercase formatting
class UppercaseFormatter(TextFormatter):

    def format_text(self, text):
        return text.upper()


# Concrete Strategy: Lowercase formatting
class LowercaseFormatter(TextFormatter):
    def format_text(self, text):
        return text.lower()


# Concrete Strategy: Title case formatting
class TitleCaseFormatter(TextFormatter):

    def format_text(self, text):
        return text.title()


# Context class
class TextEditor(object):
    def __init__(self, formatter):
        self.formatter = formatter

    def set_formatter(self, formatter):
        self.formatter = formatter

    def format_text(self, text):
        return self.formatter.format_text(text)


# Client code
if __name__ == "__main__":

    text = "This is a simple example of the Strategy Pattern."

    # Create text editor with the default uppercase formatting strategy
    editor = TextEditor(UppercaseFormatter())
    result = editor.format_text(text)
    print("Uppercase Formatting:")
    print(result)

    # Change the formatting strategy to lowercase
    editor.set_formatter(LowercaseFormatter())
    result = editor.format_text(text)
    print("\nLowercase Formatting:")
    print(result)

    # Change the formatting strategy to title case
    editor.set_formatter(TitleCaseFormatter())
    result = editor.format_text(text)
    print("\nTitle Case Formatting:")
    print(result)
```

## Template Method

```python
# Example: Template Method Pattern

# Abstract with template methods
class Notification(object):

    # Template method
    def send_notification(self, message):
        self.authenticate()
        self.format_message(message)
        self.send_message()

    # Template method
    def authenticate(self):
        print("Authentication successful")

    # Template method
    def format_message(self, message):
        print(f"Formatting message: {message}")

    # Abstract method
    def send_message(self):
        raise NotImplementedError


# Concrete Notification subclass for email
class EmailNotification(Notification):

    def send_message(self):
        print("Sending email...")


# Concrete Notification subclass for SMS
class SMSNotification(Notification):

    def send_message(self):
        print("Sending SMS...")


# Client code
if __name__ == "__main__":
    email_notification = EmailNotification()
    sms_notification = SMSNotification()

    text = "This is a notification message."

    print("Email Notification:")
    email_notification.send_notification(text)

    print("\nSMS Notification:")
    sms_notification.send_notification(text)
```

## Visitor

```python
# Example: Visitor Pattern

class ExportVisitor(object):

    def visit(self, element):
        pass


class XMLExportVisitor(ExportVisitor):

    def visit(self, element):
        print('XML exporter visiting element of type {0}'.format(type(element).__name__))


class Node(object):

    def accept(self, visitor):
        pass


class City(Node):

    def accept(self, visitor):
        visitor.visit(self)


class Industry(Node):

    def accept(self, visitor):
        visitor.visit(self)


class NavigationMap(object):

    def __init__(self):
        self.nodes = []

    def add(self, element):
        self.nodes.append(element)

    def accept(self, visitor):
        for element in self.nodes:
            element.accept(visitor)


if __name__ == "__main__":
    exporter = XMLExportVisitor()
    object_structure = NavigationMap()
    object_structure.add(City())
    object_structure.add(Industry())
    object_structure.accept(exporter)
```
