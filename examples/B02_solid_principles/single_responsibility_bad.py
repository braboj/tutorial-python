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
