import os
import time
from archiver.errors import *
from archiver.lzw import *
from archiver.huffman import *


class ArchiveManager(object):

    archivers = {
        'huff': Huffman,
        'lzw': LZW,
    }

    def __init__(self):

        # The archiver instance
        self.archiver = None

        # Internal variables used for reporting
        self.__action = ""
        self.__algorithm = ""
        self.__file_in = ""
        self.__file_in_size = 0
        self.__file_out = ""
        self.__file_out_size = 0
        self.__exec_time = 0
        self.__compress_ratio = 0

    ###############################################################################################

    @classmethod
    def __get_archiver(cls, algorithm):

        try:
            archiver_class = cls.archivers[algorithm]
            archiver_instance = archiver_class()

        except KeyError:
            raise ArchiverError

        return archiver_instance

    ###############################################################################################

    def execute(self, algorithm, action, file_in, file_out):

        self.__algorithm = algorithm
        self.__action = action
        self.__file_in = file_in
        self.__file_out = file_out

        archiver = self.__get_archiver(algorithm)

        # Start time measurement
        start_time = time.time()

        # TODO: Could be better using an action dictionary
        if action == "compress":
            text = archiver.load_text(file_in)
            compressed = archiver.compress(text)
            archiver.save_compressed(file_out, compressed)

        elif action == "decompress":
            compressed = archiver.load_compressed(file_in)
            decompressed = archiver.decompress(compressed)
            archiver.save_text(file_out, decompressed)

        else:
            raise ArchiverError

        # End time measurement
        end_time = time.time()
        self.__exec_time = end_time - start_time

        # Compress ratio calculation
        self.__file_in_size = os.stat(file_in).st_size
        self.__file_out_size = os.stat(file_out).st_size
        self.__compress_ratio = self.__file_in_size / self.__file_out_size

    ###############################################################################################

    def report(self):
        print(f" > Algorithm         = {self.__algorithm}")
        print(f" > Action            = {self.__action}")
        print(f" > FILE IN           = {self.__file_in}")
        print(f" > FILE IN_SIZE      = {self.__file_in_size} Bytes")
        print(f" > FILE OUT          = {self.__file_out}")
        print(f" > FILE OUT_SIZE     = {self.__file_out_size} Bytes")
        print(f" > EXEC_TIME         = {self.__exec_time}")
        print(f" > COMPRESS_RATIO    = {self.__compress_ratio}")
        print()
