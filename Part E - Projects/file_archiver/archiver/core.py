from abc import ABCMeta, abstractmethod
from six import with_metaclass


class AbcFileFormatter(with_metaclass(ABCMeta)):

    @classmethod
    @abstractmethod
    def write(cls, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def read(cls, *args, **kwargs):
        raise NotImplementedError


class AbcArchiver(with_metaclass(ABCMeta)):
    """ Template class for compression algorithms with partial implementation """

    def __init__(self):
        pass

    ###############################################################################################

    @abstractmethod
    def compress(self, data: str) -> list:
        raise NotImplementedError

    @abstractmethod
    def decompress(self, data: list) -> str:
        raise NotImplementedError

    ###############################################################################################

    @abstractmethod
    def load_compressed(self, filename: str, formatter: AbcFileFormatter):
        raise NotImplementedError

    @abstractmethod
    def save_compressed(self, filename: str, data: bytearray, formatter: AbcFileFormatter):
        raise NotImplementedError

    ###############################################################################################

    @staticmethod
    def load_text(filename: str) -> str:
        with open(filename, 'r') as input_file:
            data = input_file.read()
        return data

    @staticmethod
    def save_text(filename: str, data: str) -> None:
        with open(filename, "w", encoding="UTF-8") as file:
            for new_line in data:
                file.write(new_line)
