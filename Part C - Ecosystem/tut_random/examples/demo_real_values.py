import random

test = random.random()
print(test)

test = random.uniform(0, 100)
print(test)

test = random.triangular(0, 100)
print(test)

test = random.betavariate(1, 2)
print(test)

test = random.expovariate(1)
print(test)

test = random.gammavariate(1, 2)
print(test)

test = random.gauss(1, 2)
print(test)

test = random.lognormvariate(1, 2)
print(test)

test = random.normalvariate(1, 2)
print(test)

test = random.vonmisesvariate(1, 2)
print(test)

test = random.paretovariate(1)
print(test)

test = random.weibullvariate(1, 2)
print(test)