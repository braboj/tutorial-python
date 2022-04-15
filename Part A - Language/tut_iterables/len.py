test = ('a', 'b')
print(len(test))

test = ['a', 'b']
print(len(test))

test = "ab"
print(len(test))

test = {1, 2}
print(len(test))

test = {"a": 1, "b":2}
print(len(test))

test = range(10)
print(len(test))


class Session:
    def __init__(self, number=0):
        self.number = number

    def __len__(self):
        return self.number


# default length is 0
s1 = Session()
print(len(s1))

# giving custom length
s2 = Session(6)
print(len(s2))