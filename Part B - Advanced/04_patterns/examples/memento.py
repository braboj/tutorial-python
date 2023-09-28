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
