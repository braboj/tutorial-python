from archiver.core import AbcArchiver
from archiver.utils import *
from archiver.formatters import LzwFile
from archiver.definitions import *


# TODO: Taken from @YDragnev
#  - Check for algorithm
#  - Verify whether the algorithm is optimal
#  - Optimize code

class LZW(AbcArchiver):

    def __init__(self):
        super().__init__()

        self.__min_entries = LZW_MIN_ENTRIES
        self.__max_entries = LZW_MAX_ENTRIES
        self.__encoder = {chr(i): i for i in range(self.__min_entries)}
        self.__decoder = {i: chr(i) for i in range(self.__min_entries)}

    ###############################################################################################

    def load_compressed(self, filename, file_formatter=LzwFile):

        # Delegate the file operations
        with open(filename, 'rb') as input_file:
            file_struct = file_formatter.read(input_file)

        # Prepare the required data
        data = bytes_to_dict(file_struct.data)

        return data

    ###############################################################################################

    def save_compressed(self, filename, data, file_formatter=LzwFile):

        # Prepare the required data
        data_bytes = dict_to_bytes(data)

        # Delegate the concrete file operations
        with open(filename, 'wb') as file:
            file_formatter.write(
                file=file,
                data=data_bytes
            )

    ###############################################################################################

    def compress(self, uncompressed_data):

        # ???
        compressed_data = []
        string = ""

        # ???
        for symbol in uncompressed_data:
            string_plus_symbol = string + symbol
            if string_plus_symbol in self.__encoder:
                string = string_plus_symbol
            else:
                compressed_data.append(self.__encoder[string])
                if len(self.__encoder) <= LZW_MAX_ENTRIES:
                    self.__encoder[string_plus_symbol] = len(self.__encoder)
                string = symbol

        # ???
        if string in self.__encoder:
            compressed_data.append(self.__encoder[string])

        return compressed_data

    ###############################################################################################

    def decompress(self, compressed_data):

        decompressed_data = ""
        next_code = LZW_MIN_ENTRIES
        string = ""

        # ???
        for code in compressed_data:
            if code not in self.__decoder.keys():
                self.__decoder[code] = string + (string[0])
            decompressed_data += self.__decoder[code]
            if len(string) != 0:
                self.__decoder[next_code] = string + (self.__decoder[code][0])
                next_code += 1
            string = self.__decoder[code]

        return decompressed_data
