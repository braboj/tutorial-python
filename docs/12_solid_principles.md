# SOLID Principles

## Dependency Inversion Bad

```python
# Dependency Inversion Principle - Bad Example
# -------------------------------------------------------------------------------
# The Dependency Inversion Principle (DIP) dictates that high level
# modules should not depend on low level ones directly. Calculator
# instantiates Math itself and so is tightly coupled to it.


class Math(object):

        @staticmethod
        def add(a, b):
            return a + b

        @staticmethod
        def subtract(a, b):
            return a - b


class Calculator(object):

    def __init__(self):

        # Code smell: Dependency relationship is hard-coded (dependency)
        # and not abstracted (injection)

        self.math = Math()

    def add(self, a, b):
        result = self.math.add(a, b)
        return result

    def subtract(self, a, b):
        result = self.math.subtract(a, b)
        return result
```

## Dependency Inversion Good

```python
# Dependency Inversion Principle - Good Example
# -------------------------------------------------------------------------------
# The Dependency Inversion Principle (DIP) encourages depending on
# abstractions rather than concrete classes. Calculator receives an
# IMath implementation, decoupling it from a specific Math class.

class IMath(object):
    """ Simplified interface for junior math class """

    # GOOD: IMath is an abstraction that defines the contract for Math and
    # Calculator (the interface). It has no implementation details.

    @staticmethod
    def add(a, b):
        raise NotImplementedError()

    @staticmethod
    def subtract(a, b):
        raise NotImplementedError()


class Math(IMath):
    # GOOD: Both Math and Calculator depend on abstraction (MathAbc)

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b


class Calculator(object):
    """A simple calculator class

    Args:
        math (IMath): An object that implements the IMath interface

    """

    def __init__(self, math):
        # GOOD: Both Math and Calculator depend on abstraction (MathAbc)
        self.math = math

    def add(self, a, b):
        result = self.math.add(a, b)
        return result

    def subtract(self, a, b):
        result = self.math.subtract(a, b)
        return result
```

## Interface Segregation Bad

```python
# Interface Segregation Principle - Bad Example
# -------------------------------------------------------------------------------
# The Interface Segregation Principle (ISP) advises that clients
# should not be forced to depend on methods they do not use. The
# Device class defines unrelated operations that specific devices
# need to ignore.

class Device(object):

    def __init__(self, name):
        self.name = name

    def power_on(self):
        pass

    def power_off(self):
        pass

    def volume_up(self):
        # Code smell: Used only by Headset
        pass

    def volume_down(self):
        # Code smell: Used only by Headset
        pass

    def brightness_up(self):
        # Code smell: Used only by Monitor
        pass

    def brightness_down(self):
        # Code smell: Used only by Monitor
        pass


class HeadSet(Device):

    def __init__(self, name):
        super(HeadSet, self).__init__(name)

    def power_on(self):
        print("Headset powered on")

    def power_off(self):
        print("Headset powered off")

    def volume_up(self):
        print("Headset volume up")

    def volume_down(self):
        print("Headset volume down")


class Monitor(Device):

    def __init__(self, name):
        super(Monitor, self).__init__(name)

    def power_on(self):
        print("Monitor powered on")

    def power_off(self):
        print("Monitor powered off")

    def brightness_up(self):
        print("Monitor brightness up")

    def brightness_down(self):
        print("Monitor brightness down")
```

## Interface Segregation Good

```python
# Interface Segregation Principle - Good Example
# -------------------------------------------------------------------------------
# The Interface Segregation Principle (ISP) breaks large interfaces
# into focused ones. Mixins here provide only the operations each
# device actually needs.

class Device(object):
    # Defines only the common methods for all devices

    def __init__(self, name, *args, **kwargs):
        super(Device, self).__init__(*args, **kwargs)
        self.name = name

    def power_on(self):
        pass

    def power_off(self):
        pass


class SoundMixin(object):
    # Defines only the methods for all sound devices

    def __init__(self, *args, **kwargs):
        super(SoundMixin, self).__init__(*args, **kwargs)

    def volume_up(self):
        pass

    def volume_down(self):
        pass


class VisualMixin(object):
    # Defines only the methods for all visual devices

    def __init__(self, *args, **kwargs):
        super(VisualMixin, self).__init__(*args, **kwargs)

    def brightness_up(self):
        pass

    def brightness_down(self):
        pass


class TypingMixin(object):
    # Defines only the methods for all typing devices

    def __init__(self, *args, **kwargs):
        super(TypingMixin, self).__init__(*args, **kwargs)

    def press(self):
        pass

    def release(self):
        pass

    def hold(self):
        pass


class Keyboard(Device, TypingMixin):
    pass


class HeadSet(Device, SoundMixin):
    pass


class Speaker(Device, SoundMixin):
    pass


class Monitor(Device, VisualMixin):
    pass


class Television(Device, SoundMixin, VisualMixin):
    pass


class Computer(Device, SoundMixin, VisualMixin, TypingMixin):
    pass
```

## Liskov Substitution Bad

```python
# Liskov Substitution Principle - Bad Example
# -------------------------------------------------------------------------------
# The Liskov Substitution Principle (LSP) requires that subclasses
# can stand in for their base class. Here the work method checks
# for `Baby` explicitly, so `Baby` cannot substitute `Human`.

class Human(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{} eating".format(self.name))

    def sleep(self):
        print("{} sleeping".format(self.name))

    def work(self):

        # Code smell: Type checking or conditional logic to determine the
        # behaviour and thus the child class and the parent class are not
        # substitutable. We have junior divergent behaviour for Human and Baby
        # when the work method is called.

        if type(self) == Baby:
            raise RuntimeError("Too young to work")

        print("{} working".format(self.name))


class Baby(Human):

    def suckle(self):
        print("{} suckling".format(self.name))
```

## Liskov Substitution Good

```python
# Liskov Substitution Principle - Good Example
# -------------------------------------------------------------------------------
# The Liskov Substitution Principle (LSP) means that objects of a
# superclass should be replaceable with objects of its subclasses
# without breaking the program. Each subclass here simply extends
# Human without special checks.

class Human(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{} eating".format(self.name))

    def sleep(self):
        print("{} sleeping".format(self.name))


class Adult(Human):

    # GOOD: Adult can be substituted for Human because it implements all the
    # methods of the Human class and it does not violate the Liskov
    # Substitution Principle.

    def work(self):
        print("{} working".format(self.name))


class Baby(Human):

    # GOOD: Baby can be substituted for Human because it implements all the
    # methods of the Human class and it does not violate the Liskov
    # Substitution Principle.

    def suckle(self):
        print("{} suckling".format(self.name))
```

## Open Closed Bad

```python
# Open/Closed Principle - Bad Example
# -------------------------------------------------------------------------------
# The Open/Closed Principle (OCP) states that code should be open for
# extension but closed for modification. Adding a new format here
# requires changing the FileProcessor class, so OCP is violated.

class FileProcessor(object):

    def __init__(self, file_format="upper"):
        self.format = file_format
        self.data = ""

    def process(self, text):

        # This violates the Open/Closed Principle because junior new file format
        # cannot be added without modifying the FileProcessor class.

        if self.format == "upper":
            # Responsibility: Process the data
            self.data = text.upper()

        elif self.format == "lower":
            # Responsibility: Process the data
            self.data = text.lower()

        else:
            raise ValueError("Invalid format: {}".format(format))

        return self.data


process = FileProcessor(file_format="upper")
print(process.process("Hello World!"))
```

## Open Closed Good

```python
# Open/Closed Principle - Good Example
# -------------------------------------------------------------------------------
# The Open/Closed Principle (OCP) says that classes should be
# extendable without needing to modify their source. FileProcessor
# composes formatter objects so new behaviour can be added safely.

class LowercaseFormat(object):

    @staticmethod
    def process(text):
        return text.lower()


class UppercaseFormat(object):
    # Responsibility: Process the data

    @staticmethod
    def process(text):
        return text.lower()


# Add more file formats here...

class FileProcessor(object):

    # Use composition to extend the functionality of the FileProcessor class
    # without modifying the class itself.

    def __init__(self, file_format):
        self.formatter = file_format
        self.data = ""

    def process(self, text):
        self.data = self.formatter.process(text)
        return self.data


processor = FileProcessor(LowercaseFormat())
print(processor.process("Hello World!"))
```

## Single Responsibility Bad

```python
# Single Responsibility Principle - Bad Example
# -------------------------------------------------------------------------------
# The Single Responsibility Principle (SRP) says that a class should
# have only one reason to change. This example bundles reading,
# writing and processing into one class, so it breaks SRP.

class MyCustomFileFormat(object):
    """ This class violates the Single Responsibility Principle because:

        1. It reads the file and stores the data
        2. It writes data to the file
        3. It processes the stored data

    """

    def __init__(self, filename):
        self.filename = filename
        self.data = ""

    def read(self):
        # Responsibility: Read the file
        with open(self.filename, "r") as f:
            self.data = f.read()
            return self.data

    def write(self, text):
        # Responsibility: Write to the file
        with open(self.filename, "w") as f:
            f.write(text)

    def process(self):
        # Responsibility: Process the data
        self.data = self.data.upper()
        return self.data


# Create the file reader
reader = MyCustomFileFormat("test_input.myformat")
print(reader.read())

# Process the data
print(reader.process())

# Create the file writer
writer = MyCustomFileFormat("test_output.myformat")
writer.write(reader.data)
```

## Single Responsibility Good

```python
# Single Responsibility Principle - Good Example
# -------------------------------------------------------------------------------
# The Single Responsibility Principle (SRP) states that a class should
# do only one thing. Here the reading, writing and processing logic
# are split into separate classes.

# By splitting the class into three classes, we can now reuse the classes in
# other parts of the program. A change in one class will not affect the other
# classes. This makes the code more maintainable and easier to understand.

class MyCustomFileFormatReader(object):
    # Responsibility: Read the file

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            return f.read()


class MyCustomFileFormatWriter(object):
    # Responsibility: Write to the file

    def __init__(self, filename):
        self.filename = filename

    def write(self, text):
        with open(self.filename, "w") as f:
            f.write(text)


class FileProcessor(object):
    # Responsibility: Process the data

    def __init__(self):
        self.data = ""

    def process(self, data):
        self.data = data.lower()
        return self.data


# Create the file reader
reader = MyCustomFileFormatReader("test_input.myformat")
content = reader.read()
print(content)

# Process the data
processor = FileProcessor()
new_content = processor.process(content)
print(new_content)

# Create the file writer
writer = MyCustomFileFormatWriter("test_output.myformat")
writer.write(new_content)
```
