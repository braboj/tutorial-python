import heapq
from archiver.core import AbcArchiver
from archiver.utils import *
from archiver.formatters import HuffmanFile


# TODO: Taken from @YDragnev
#  - Check for algorithm
#  - Verify whether the algorithm is optimal
#  - Optimize code


class HeapNode(object):
    """ Help class for calculating node frequency in the tree. """

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HeapNode):
            return False
        return self.freq == other.freq


class Huffman(AbcArchiver):

    def __init__(self):

        super().__init__()

        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}
        self.full_tree = False

    ###############################################################################################

    @staticmethod
    def make_frequency_dict(text):
        """ Calculate the frequency of each letter in the file. """

        frequency = {}
        for character in text:
            if character not in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    ###############################################################################################

    def make_heap(self, frequency):
        """ Fill the heap queue with tree nodes. """

        for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)
        if len(self.heap) > 1:
            self.full_tree = True

    ###############################################################################################

    def merge_nodes(self):
        """ Merge each two nodes in one new, equal to the sum of them. """

        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    ###############################################################################################

    def make_codes_helper(self, root, current_code):
        """ A help method for each node code making. """

        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    ###############################################################################################

    def make_codes(self):
        """ Make binary code for each node. """

        root = heapq.heappop(self.heap)
        current_code = ""
        if not self.full_tree:
            current_code = "0"
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        """ Make the string for archived file."""

        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    ###############################################################################################

    @staticmethod
    def pad_encoded_text(encoded_text):
        """ Pads necessary quantity of bits to the end of encoded text so its length to be multiple
        of 8 (one byte has 8 bits).
        The key for number of padded symbols in the end is added to the beginning of the encoded
        text as <padded info>.
        """

        extra_padding = 8 - len(encoded_text) % 8
        for _ in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text

        return encoded_text

    ###############################################################################################

    @staticmethod
    def get_byte_array(padded_encoded_text):
        """ Makes encoded string in bits to a new encoded string in bytes. """

        if len(padded_encoded_text) % 8 != 0:
            print("Encoded text not padded properly")
            exit(0)

        byte_array = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            byte_array.append(int(byte, 2))
        return byte_array

    ###############################################################################################

    @staticmethod
    def remove_padding(padded_encoded_text):
        """ Removes the padded bits from the string taken off the archived file. """

        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1 * extra_padding]

        return encoded_text

    ###############################################################################################

    def decode_text(self, encoded_text):
        """ Decode the input text string from compressed file. """

        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    ###############################################################################################

    def load_compressed(self, filename, file_parser=HuffmanFile):

        with open(filename, 'rb') as input_file:
            file_struct = file_parser.read(input_file)

        return file_struct.tree, file_struct.data

    ###############################################################################################

    def save_compressed(self, filename, data, file_parser=HuffmanFile):

        # Prepare the basic elements needed to be written in the file
        tree_data = dict_to_bytes(self.reverse_mapping)
        data_bytes = data

        with open(filename, 'wb') as file:

            # Create the file structure
            file_parser.write(
                file=file,
                tree=tree_data,
                data=data_bytes
            )

    ###############################################################################################

    def compress(self, uncompressed_data):

        frequency = self.make_frequency_dict(uncompressed_data)
        self.make_heap(frequency)
        self.merge_nodes()
        self.make_codes()

        bytestream = self.get_encoded_text(uncompressed_data)
        padded_bytestream = self.pad_encoded_text(bytestream)
        compressed_data = self.get_byte_array(padded_bytestream)

        return bytes(compressed_data)

    ###############################################################################################

    def decompress(self, compressed_data):

        tree_bytes = compressed_data[0]
        data_bytes = compressed_data[1]

        # Get the huffman tree from compressed data
        self.reverse_mapping = bytes_to_dict(tree_bytes)

        # Get the bitstring from the compressed data
        bit_string = hex_to_bin(data_bytes)
        encoded_text = self.remove_padding(bit_string)
        decompressed_data = self.decode_text(encoded_text)

        return decompressed_data


