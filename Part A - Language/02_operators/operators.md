# Arithmetic

The arithmetic operators are the most basic expressions in Python. 

```
Addition        :   5 + 3   = 8         :   Addition of two numbers
Substraction    :   5 - 3   = 2         :   Substraction of two numbers
Multiplication  :   5 * 3   = 15        :   Multiplication of two numbers
Division        :   5 / 3   = 1         :   Float division of two numbers
Floor division  :   5 // 2  = 2         :   Integer division of two numbers
Modulus         :   5 % 3   = 2         :   Remainder after divison of two numbers
Exponentiation  :   5 ** 3  = 125       :   Exponentiation with base and exponent

```

Examples:

```python

x = 5.0
y = 3.0
print(x / y)
print(x // y)
print(x % y)

print('-' * 80)

x = -5.0
y = 3.0
print(x / y)
print(x // y)
print(x % y)
```


# Comparison

The comparision operators are used in expressions comparing different values. The result will be 
either `True` or `False`.

```
Equal                       :   x == 1
Not equal                   :   x != 1 
Greater than                :   x > 1
Greater than or equal to    :   x >= 1
Less than                   :   x < 1
Less than or equal to       :   x <= 1
Between                     :   1 < x < 2
```

Examples:

```python
x = 1
y = 2
print(x > y)
print(x < y)
print(1 < x < 3)
```

# Logical

The logical operators are used to control the flow of the program. The result will be either 
`True` or `False`.

```
NOT     :   not x 
AND     :   x and y
OR      :   x or y
```

Examples:

```python
x = 1
y = 2

print(not x)
print(x and y)
print(x or y)
```

# Identity

The identity operators are used to compare objects and check if two objects are identical.

```
is          :   x is y      :   True if x and y are the same object
is not      :   x is not y  :   True if x and y are different objects
```

# Membership

The membership operators are used check if an object is part of a collection of objects.

```
in          :   x in y      :   True if x is present in y
not in      :   x not in y  :   True if x is not present in y
```

# Bitwise

The bitwise operators are used for setting individual bits in a byte, word and other integer 
types.

```
AND             :   x & y   :   1010 & 0101 = 0000, 1001 & 1111 = 1001 
OR              :   x | y   :   1010 & 0101 = 1111, 1001 & 1111 = 1111
XOR             :   x ^ y   :   1010 & 0101 = 0000, 1001 & 1111 = 0110
NOT             :   ~x      :   ~1010 = 0101 
Left shift      :   x << 1  :   1010 << 1 = 0100
Right shift     :   x >> 1  :   1010 >> 1 = 0101
```

```python
x = int('1010', 2)
print(bin(x >> 1))
```

# Conditional

The only ternary conditional statement in Python allows quick verification of a given condition and
performing an action depending on the result of the check.

```python
a, b = 10, 20
 
# Copy value of a in min if a < b else copy b
min = a if a < b else b
print(min)
```

# Assignement

The assignement operator is used to change the value of a given variable. Python offers a variety
of assignement operators, often combining arithmetic or bitwise operations and assignement in 
one statement.

```python
x = 1       x = 1
x += 1      x = x + 1
x -= 1      x = x - 1
x *= 1      x = x * 1
x /= 1      x = x / 1
x %= 1      x = x % 1    
x //= 1     x = x // 1
x **= 1     x = x ** 1
x &= 1      x = x & 1
x |= 1      x = x | 1
x ^= 1      x = x ^ 1
x >>= 1     x = x >> 1
x <<= 1     x = x << 1
```