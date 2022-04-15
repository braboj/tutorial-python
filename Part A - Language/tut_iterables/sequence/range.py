from pprint import pprint

result = range(1, 10, 2)
pprint(dir(result))

try:
    iterator = iter(result)

    while True:
        try:
            print(next(iterator), sep=' ', end=' ')
        except StopIteration:
            break

except TypeError as te:
    print(result, 'is not iterable')

print('')
print(result.count(5))
print(result.index(5))
print(result.start)
print(result.stop)
print(result.step)

