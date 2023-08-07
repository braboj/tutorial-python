def power_of(n):
    def power(x):
        return x ** n
    return power


# Multiplier of 3
sqrt = power_of(0.5)

# Multiplier of 5
sqr = power_of(2)

print(sqrt(100.0))
print(sqr(10.0))