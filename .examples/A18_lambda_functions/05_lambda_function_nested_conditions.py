# Lambda function with nested conditionals
# --------------------------------------------------------------------------------
# This lambda expression checks two ranges using nested conditional operators.
# It returns ``1`` when the argument exceeds 10 or falls below -10 and ``0`` in
# all other cases. The expression remains concise despite the multiple branches.

z = lambda c: 1 if c > 10 else (1 if c < -10 else 0)
print(-11, -10, -1, 0, 1, 10, 11, sep='\t')
print(z(-11), z(-10), z(-1), z(0), z(1), z(10), z(11), sep='\t')
