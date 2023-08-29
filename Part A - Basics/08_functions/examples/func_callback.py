# Example: Callback function

def button_action(x):
    print("Callback function called with {}".format(x))


def on_pressed(callback):
    print("Test function called")
    callback("ON")


def off_pressed(callback):
    print("Test function called")
    callback("OFF")


on_pressed(callback=button_action)
off_pressed(callback=button_action)
