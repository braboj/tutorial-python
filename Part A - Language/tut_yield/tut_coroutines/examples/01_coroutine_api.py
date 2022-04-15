def letter_generator(text):
    print("Started")
    position = 0
    try:
        while True:
            try:
                offset = yield text[position]

                if offset is None:
                    position += 1
                else:
                    position = offset

            except ValueError:
                print("Value error on position = " + str(position))

    except GeneratorExit:
        print("Terminated")


letter = letter_generator("abc")

# Generate letters
print(next(letter))
print(next(letter))

# Reset generator and generate letter
print(letter.send(0))

# Generate a next letter
print(next(letter))

# Throw an exception to the generator
print(letter.throw(ValueError))

# Throw GeneratorExit to the generator
letter.close()

