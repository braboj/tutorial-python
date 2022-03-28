test = [1, 2, 3, 4, 5]

result = [1 if x % 2 == 0 else 0 for x in test]
print(test)
print(result)

result = []
for x in test:
    if x % 2 == 0:
        result.append(1)
    else:
        result.append(0)

print(test)
print(result)

result = [1 if x % 2 == 0 else (-1 if x % 3 == 0 else 0) for x in test]
print(test)
print(result)

result = []
for x in test:
    if x % 2 == 0:
        result.append(1)
    elif x % 3 == 0:
        result.append(-1)
    else:
        result.append(0)

print(test)
print(result)

x = (1, 2, 3)
y = [p * p for p in x]
print(y)
