import random


def make_repeated_symbol(symbol='A', n=100):
    return symbol * n


def make_repeated_pattern(pattern='ABC', n=100):
    return pattern * n


def make_white_noise(n=100):
    random_text = ""
    for i in range(n):
        chr_code = random.randrange(32, 126)
        chr_to_add = chr(chr_code)
        random_text += chr_to_add

    return random_text


with open('test.txt', 'w') as f:
    # Uncomment the desired row to generate the file
    data = make_repeated_symbol(symbol='A', n=100)
    # data = make_repeated_pattern(pattern='ABC', n=100)
    # data = make_white_noise(100)
    f.write(data)
