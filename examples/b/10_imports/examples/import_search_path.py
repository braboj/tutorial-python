# Example: Import Search Path

import sys
import pprint

from api import submodule1
print('submodule1.my_id =', submodule1.my_id)

# Print the search path
paths = sys.path
for path in paths:
    print(path)

print()

# Add the current directory to the search path
sys.path.append('.')
paths = sys.path
for path in paths:
    print(path)
