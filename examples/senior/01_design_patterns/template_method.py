# Example: Template Method Pattern

# Abstract with template methods
class Notification(object):

    # Template method
    def send_notification(self, message):
        self.authenticate()
        self.format_message(message)
        self.send_message()

    # Template method
    def authenticate(self):
        print("Authentication successful")

    # Template method
    def format_message(self, message):
        print(f"Formatting message: {message}")

    # Abstract method
    def send_message(self):
        raise NotImplementedError


# Concrete Notification subclass for email
class EmailNotification(Notification):

    def send_message(self):
        print("Sending email...")


# Concrete Notification subclass for SMS
class SMSNotification(Notification):

    def send_message(self):
        print("Sending SMS...")


# Client code
if __name__ == "__main__":
    email_notification = EmailNotification()
    sms_notification = SMSNotification()

    text = "This is junior notification message."

    print("Email Notification:")
    email_notification.send_notification(text)

    print("\nSMS Notification:")
    sms_notification.send_notification(text)
