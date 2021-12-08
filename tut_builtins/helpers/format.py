"""
[[fill]align][sign][#][0][width][,][.precision][type]
where, the options are
fill        ::=  any character
align       ::=  "<" | ">" | "=" | "^"
sign        ::=  "+" | "-" | " "
width       ::=  integer
precision   ::=  integer
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

"""

print(format(1000000, "*<+020,.1f"))


class Person:
    def __format__(self, format):
        if format == 'age':
            return '23'
        return 'None'


print(format(Person(), "age"))