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
