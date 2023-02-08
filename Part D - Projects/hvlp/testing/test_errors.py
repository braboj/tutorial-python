# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from components.errors import *


###################################################################################################
# MODULE TESTS
###################################################################################################

def test_error():

    test = HvlpError(message='test message', reason='test reason')
    try:
        raise test

    except HvlpError as e:
        logging.info("The exception has message `{0}` and reason `{1}`".format(e.message, e.reason))
        assert (e.message == test.message and e.reason == test.reason)


def test_error_message():

    test = HvlpConnectionError()
    try:
        raise test

    except HvlpError as e:
        logging.info("The exception has message `{0}` and reason `{1}`".format(e.message, e.reason))
        assert (e.message == test.message)
        pass


def test_error_reason():

    test = HvlpConnectionError(reason='Missing Socket')
    try:
        raise test

    except HvlpError as e:
        logging.info("The exception has message `{0}` and reason `{1}`".format(e.message, e.reason))
        assert (e.message == test.message)
        pass


###################################################################################################
# MAIN
###################################################################################################

if __name__ == "__main__":

    logging.basicConfig(format=b'%(asctime)s - %(funcName)-25s: %(message)s', level=logging.INFO)
    test_error()
    test_error_message()
    test_error_reason()
