# Code that works in both Python 2 and 3
from six.moves import input
prompt = input()
prompt = prompt.encode('utf-8')
print(prompt)