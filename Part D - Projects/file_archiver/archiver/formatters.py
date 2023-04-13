from archiver.core import *


class LzwFile(AbcFileFormatter):
    """ Raw binary file without headers used by LZW or similar algorithms """

    def __init__(self, data):
        self.data = data

    @classmethod
    def write(cls, file, data):
        file.write(data)

        return cls(
            data=data,
        )

    @classmethod
    def read(cls, file):
        data = file.read()

        return cls(
            data=data,
        )


class HuffmanFile(AbcFileFormatter):
    """ Structured binary file with headers used by Huffman """

    #   4 Bytes     | NNN   |   4 Bytes     | MMM
    # TREE_LENGTH   | TREE  | DATA_LENGTH   | DATA

    # Size of tree length in bytes
    TREE_LENGTH = 4

    # Size of data length in bytes
    DATA_LENGTH = 4

    def __init__(self, tree_len, tree, data_len, data):
        self.tree_len = tree_len
        self.tree = tree
        self.data_len = data_len
        self.data = data

    @classmethod
    def write(cls, file, tree, data):

        tree_len = len(tree).to_bytes(length=cls.TREE_LENGTH, byteorder='big')
        data_len = len(data).to_bytes(length=cls.DATA_LENGTH, byteorder='big')

        file.write(tree_len)
        file.write(tree)
        file.write(data_len)
        file.write(data)

        return cls(
            tree_len,
            tree,
            data_len,
            data=data,
        )

    @classmethod
    def read(cls, file):

        tree_len = int.from_bytes(file.read(cls.TREE_LENGTH), byteorder='big')
        tree = file.read(tree_len)
        data_len = int.from_bytes(file.read(cls.DATA_LENGTH), byteorder='big')
        data = file.read(data_len)

        return cls(
            tree_len,
            tree,
            data_len,
            data=data,
        )
