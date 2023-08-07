# coding: utf-8
from __future__ import print_function
from __future__ import unicode_literals

import logging
from abc import ABCMeta
from six import with_metaclass

# Add the local directories to the system path
import sys
sys.path.append(str("."))
sys.path.append(str(".."))

# Local packages
from errors import *


class CanFrameTemplate(with_metaclass(ABCMeta)):
    """ A template class for CAN frames.

    Args:
        can_id  : The 11-bit or 29-bit CAN identifier of the frame
        data    : the data contains in the frame
        rtr     : Remote transmission request (RTR)
        max_id  : The maximum possible id number for the specific frame

    Examples:

        # Basic can frame
        message = CanFrameBasic(can_id=0x05, data=[0x00, 0x4B, 0x03, 0x01, 0x01])

        # Extended CAN frame with RTR
        message = CanFrameExtended(can_id=0x05, data=[0x00, 0x4B, 0x03, 0x01, 0x01], rtr=True)

    """

    MAX_CAN_ID = 0x7FF
    DATA_MIN_LENGTH = 0
    DATA_MAX_LENGTH = 8

    def __init__(self, can_id=0, data=None, rtr=False, max_id=MAX_CAN_ID):
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.addHandler(logging.NullHandler())

        # Initialize private attributes
        self._can_id = 0
        self._length = 0
        self._data = []
        self._rtr = False

        # Sets the maximum id of the frame
        self.max_id = max_id

        # Address validation
        self.can_id = can_id

        # Remote transmission request (RTR) validation
        self.rtr = bool(rtr)

        # Data validation
        if data is None:
            self.data = []
        else:
            self.data = list(data)

    ##########################################################################################

    def __repr__(self):
        """ String represention of the object used for logging puproses"""

        if self.rtr:
            result = "0x{0:X}:{1}:RTR".format(self.can_id, [hex(b) for b in self.data])
        else:
            result = "0x{0:X}:{1}".format(self.can_id, [hex(b) for b in self.data])

        return result

    ##########################################################################################

    def __eq__(self, other):
        """ Compares two frames and returns True if the CAN-ID and the DATA field match """

        result = True
        result = result & (self.can_id == other.can_id)
        result = result & (tuple(self.data) == tuple(other.data))
        return result

    def __ne__(self, other):
        """ Compares two frames and returns True if the CAN-ID and the DATA field differ """

        return not self.__eq__(other)

    ##########################################################################################

    @property
    def can_id(self):
        """ Get/Sets the CAN-ID with range check """
        return self._can_id

    @can_id.setter
    def can_id(self, value):
        if value > self.max_id:
            raise CanBusAddressError
        else:
            self._can_id = value

    ##########################################################################################

    @property
    def length(self):
        """ Get/Sets the frame length with range check and cut off to 8 bytes if needed. """
        return self._length

    @length.setter
    def length(self, value):
        self._length = min(value, self.DATA_MAX_LENGTH)

    ##########################################################################################

    @property
    def data(self):
        # Defining specific data
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.length = len(value)

    ##########################################################################################

    def report(self):
        # Creates a report for the defined frame
        self.log.info("MESSAGE_ID   = {0}".format(self.can_id))
        self.log.info("LENGTH       = {0}".format(self.length))
        self.log.info("DATA         = {0}".format(self.data))
        self.log.info("RTR         = {0}".format(self.rtr))

    ##########################################################################################

    @property
    def rtr(self):
        # Setting the RTR value
        return self._rtr

    @rtr.setter
    def rtr(self, value):
        self._rtr = value

    ##########################################################################################


class CanFrameBasic(CanFrameTemplate):
    """ Class representation of the basic CAN frame. Can frame ID is 11 bit long.

    Args:
        can_id  : The 11-bit CAN identifier of the frame
        data    : the data contains in the frame
        rtr     : Remote transmission request (RTR)

    """

    # The last valid CAN-ID
    MAX_CAN_ID = 0x7FF

    def __init__(self, can_id=0, data=None, rtr=False):
        super(CanFrameBasic, self).__init__(can_id=can_id, data=data, rtr=rtr, max_id=self.MAX_CAN_ID)

    ##########################################################################################


class CanFrameExtended(CanFrameTemplate):
    """ Class representation of the extended CAN frame. Can frame ID is 29 bit long.

    Args:
        can_id  : The 29-bit CAN identifier of the frame
        data    : the data contains in the frame
        rtr     : Remote transmission request (RTR)
    """

    # The last valid CAN-ID
    MAX_CAN_ID = 0x1FFFFFFF

    def __init__(self, can_id=0, data=None, rtr=False):
        super(CanFrameExtended, self).__init__(can_id=can_id, data=data, rtr=rtr, max_id=self.MAX_CAN_ID)
