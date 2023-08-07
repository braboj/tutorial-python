# coding: utf-8
from __future__ import print_function
from __future__ import unicode_literals

# Add the local directories to the system path
import sys
sys.path.append(str("."))
sys.path.append(str(".."))


class CanBusError(Exception):
    """ Generic CAN bus error """

    def __init__(self, message, extended_info):
        self.message = message
        self.extended_info = extended_info

    def __str__(self):
        if self.extended_info:
            result = self.message + " : " + self.extended_info
        else:
            result = self.message

        return result


class CanBusDataLengthError(CanBusError):
    """ The data length is not valid"""

    def __init__(self, message="The data length is not valid !"):
        super(CanBusDataLengthError, self).__init__(
            message="CAN Error.",
            extended_info=message
        )


class CanBusAddressError(CanBusError):
    """ The CAN-ID is not valid """

    def __init__(self, message="The CAN-ID is not valid !"):
        super(CanBusAddressError, self).__init__(
            message="CAN Error.",
            extended_info=message
        )
