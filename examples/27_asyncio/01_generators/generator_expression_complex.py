# Example: Complex generator expression with the the ternary operator (if-else)

# Yield "apple" if number is even else yield "pie"
generator = (("apple" if i % 2 == 0 else "pie") for i in range(6))
for x in generator:
    print(x)