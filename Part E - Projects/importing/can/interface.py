# coding: utf-8
from __future__ import print_function
from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod
from six import with_metaclass

# Add the local directories to the system path
import sys
sys.path.append(str("."))
sys.path.append(str(".."))


##############################################################################################
# Abstract interface for CAN adapters
##############################################################################################

class CanNodeABC(with_metaclass(ABCMeta)):

    def __init__(self, device):

        # Device instance to be adapted
        self.device = device

    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def configure(self, node_id, baudrate):
        raise NotImplementedError

    @abstractmethod
    def deconfigure(self):
        raise NotImplementedError

    @abstractmethod
    def start_listen(self, can_id):
        raise NotImplementedError

    @abstractmethod
    def stop_listen(self, can_id):
        raise NotImplementedError

    @abstractmethod
    def send(self, frame):
        raise NotImplementedError

    @abstractmethod
    def recv(self):
        raise NotImplementedError

    @abstractmethod
    def flush(self):
        raise NotImplementedError
