# Example : A bad example that violates the Open/Closed Principle

class FileProcessor(object):

    def __init__(self, file_format="upper"):
        self.format = file_format
        self.data = ""

    def process(self, text):

        # This violates the Open/Closed Principle because a new file format
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
