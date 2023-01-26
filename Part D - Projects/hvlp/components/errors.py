class HvlpError(Exception):
    pass

class HvlpConnectionError(HvlpError):

    def __init__(self):
        self.message = "No connection to the broker"

    def __str__(self):
        return self.message


class HvlpFormatError(HvlpError):

    def __init__(self):
        self.message = "Empty or malformed message received"

    def __str__(self):
        return self.message


class HvlpCommandError(HvlpError):

    def __init__(self):
        self.message = "Unknown Command"

    def __str__(self):
        return self.message

class HvlpArgumentsError(HvlpError):

    def __init__(self):
        self.message = "Missing arguments"

    def __str__(self):
        return self.message