# Open/Closed Principle - Good Example
# ------------------------------------------------------------------------------
# The Open/Closed Principle (OCP) says that classes should be
# extendable without needing to modify their source.
#
# By using composition, we can extend the functionality of the FileProcessor
# class without changing its code. This allows us to add new file formats
# without modifying the existing class, adhering to the OCP.

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
