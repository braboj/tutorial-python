def odd_flag(text):

    result = []

    # Take only odd numbers
    for index, char in enumerate(text):
        if index % 2 != 0:
            result.append(char)

    result = "".join(result)

    print(result)
    return result


def cut(text, start, length):
    result = text[:start] + text[(start + length):]
    result = "".join(result)

    print(result)
    return result


def substitute(text, symbol1, symbol_2):
    result = text
    if symbol1 in text:
        result = text.replace(symbol1, symbol_2)
        result = "".join(result)
        print(result)
    else:
        print("Nothing to replace!")

    return result


password = input()
line = ''

while line != "Done":

    arguments = line.split(" ")
    command = arguments[0]

    if command == "TakeOdd":
        password = odd_flag(password)

    elif command == "Cut":
        offset = int(arguments[1])
        length = int(arguments[2])
        password = cut(password, offset, length)

    elif command == "Substitute":
        symbol1 = arguments[1]
        symbol2 = arguments[2]
        password = substitute(password, symbol1, symbol2)

    else:
        pass

    line = input()

# final print
password = "".join(password)
print(f"Your password is: {password}")
