# strategy

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
