# single_responsibility_good

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
