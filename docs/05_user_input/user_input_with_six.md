# user_input_with_six

```python
# Cross-Version User Input with six
# --------------------------------------------------------------------------------
# If the code needs to work in both Python 2 and 3, you can use the `six`
# library to handle user input.

from six.moves import input

prompt = input('Enter something: ')
print(prompt)
# Output: <user input in bytes>
```
