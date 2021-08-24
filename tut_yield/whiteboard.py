# Implementation with a colllection
def evens_A(stream):
    them = []
    for n in stream:
        if n % 2 == 0:
            them.append(n)
    return them


# Implementaton with a generator
def evens_B(stream):
    for n in stream:
        if n % 2 == 0:
            yield n


num = [x for x in range(10)]

print("-" * 80)
for x in evens_A(num):
    print(x)

print("-" * 80)
for x in evens_B(num):
    print(x)