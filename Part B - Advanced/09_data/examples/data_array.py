# Example: Array of data

import array


def test_int():

    # Create an array of integers
    int_array = array.array('i', [1, 2, 3, 4, 5])

    # Convert the array to a bytes object (useful for binary data)
    bytes_data = int_array.tobytes()
    print(bytes_data)

    # Convert a bytes object back to an array
    new_array = array.array('i')
    new_array.frombytes(bytes_data)
    print(new_array)

    print()


def test_unicode():

    # Use unicode characters
    unucode_array = array.array('u', "Здравейте, хора!")

    # Convert the array to a bytes object (useful for binary data)
    bytes_data = unucode_array.tobytes()
    print(bytes_data)

    # Convert a bytes object back to an array
    new_array = array.array('u')
    new_array.frombytes(bytes_data)
    print(new_array)

    print()


if __name__ == "__main__":
    test_int()
    test_unicode()
