# Example: Decorator Pattern

from abc import ABC, abstractmethod


class NotifierAbc(ABC):

    @abstractmethod
    def notify(self):
        pass


class Notifier(NotifierAbc):

    def notify(self):
        print("Print on screen ...")


class NotifierDecorator(NotifierAbc):

    def __init__(self, component):
        self._component = component

    @abstractmethod
    def notify(self):
        pass


class EmailNotifier(NotifierDecorator):

    @staticmethod
    def send_email():
        print("Sending email ...")

    def notify(self):
        self.send_email()
        self._component.notify()


class SMSNotifier(NotifierDecorator):

    @staticmethod
    def send_sms():
        print("Sending SMS ...")

    def notify(self):
        self.send_sms()
        self._component.notify()


def main():
    notifier = Notifier()
    notifier_with_email = EmailNotifier(notifier)
    notifier_with_email_and_sms = SMSNotifier(notifier_with_email)
    notifier_with_email_and_sms.notify()


if __name__ == "__main__":
    main()
