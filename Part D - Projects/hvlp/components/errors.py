# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import logging


class HvlpError(Exception):

    def __init__(self, message, reason):
        self.message = message
        self.reason = reason
        self.separator = ":"

    def __str__(self):

        # Additional information to the base message
        if self.reason:
            result = self.message + " " + self.separator + " " + self.reason

        # Only the base message
        else:
            result = self.message

        return result


class HvlpParsingError(HvlpError):

    def __init__(self, reason=""):
        super(HvlpParsingError, self).__init__(
            message="The stream is empty or cannot be converted to bytes",
            reason=reason
        )


class HvlpConnectionError(HvlpError):

    def __init__(self, reason=""):
        super(HvlpConnectionError, self).__init__(
            message="The client is not connected to the broker",
            reason=reason
        )


class HvlpAlreadyConnected(HvlpError):

    def __init__(self, reason=""):
        super(HvlpAlreadyConnected, self).__init__(
            message="The client is already connected to the broker",
            reason=reason
        )


class HvlpPayloadFormatError(HvlpError):

    def __init__(self, reason=""):
        super(HvlpPayloadFormatError, self).__init__(
            message="The allowed values for each byte are in the range 0-255",
            reason=reason
        )


class HvlpCommandError(HvlpError):

    def __init__(self, reason=""):
        super(HvlpCommandError, self).__init__(
            message="Unknown Command",
            reason=reason
        )


class HvlpArgumentsError(HvlpError):

    def __init__(self, reason=""):
        self.message = "Missing arguments " + ":" + reason + ")"


if __name__ == "__main__":
    logging.basicConfig(format=b'%(asctime)s - %(funcName)-30s: %(message)s', level=logging.INFO)
