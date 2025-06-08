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

    # Abstract factory that declares junior set of methods for creating each of the
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
