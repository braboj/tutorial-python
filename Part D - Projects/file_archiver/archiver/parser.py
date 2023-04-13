import argparse


class UserInput(object):

    @staticmethod
    def parse():

        parser = argparse.ArgumentParser()

        parser.add_argument('--file_in', type=str, required=True,
                            help='Input file for operation')

        parser.add_argument('--file_out', type=str, required=True,
                            help='Output file for operation')

        parser.add_argument('--alg', type=str, required=False, default='huff',
                            help='Compression type: Huffman(huff) or LZW(lzw)')

        parser.add_argument('--action', type=str, required=True,
                            help='Decompression type: compress or decompress')

        args = parser.parse_args()

        file_in = args.file_in
        file_out = args.file_out
        algorithm = args.alg
        action = args.action

        return algorithm, action, file_in, file_out


if __name__ == "__main__":
    arguments = UserInput.parse()
    print(arguments)
