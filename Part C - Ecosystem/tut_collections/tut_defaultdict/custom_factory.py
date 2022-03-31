import collections


def string_factory():
    return 'default'


def constant_factory(value):
    return lambda: value


d = collections.defaultdict(string_factory)
print('a =>', d['a'])
print('b =>', d['b'])

d = collections.defaultdict(constant_factory(1))
print('a =>', d['a'])
print('b =>', d['b'])

