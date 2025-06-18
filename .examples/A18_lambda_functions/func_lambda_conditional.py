# Conditional lambda
# --------------------------------------------------------------------------------
# A lambda can contain a conditional expression to produce different values
# based on its input. This one returns ``1`` when the argument is positive and
# ``0`` otherwise. Such compact expressions are useful for simple
# transformations.
y = lambda b: 1 if b > 0 else 0
print(y(-1), y(0), y(1))
