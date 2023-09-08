# Example: Mediator Pattern


# Mediator interface
class Mediator(object):

    def forward(self, message, colleague):
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


# Colleague interface
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


# Concrete Colleague
class Textbox(Component):

    def send(self, message):
        print(f"Textbox sends: {message}")
        self.mediator.forward(message, self)

    def receive(self, message):
        print(f"Textbox receives: {message}")


# Concrete Colleague
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