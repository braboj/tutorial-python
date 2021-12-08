from collections import defaultdict

# Phase 1: Manual initialization when key is missing

dict_set = {}
if "a" not in dict_set:
    dict_set["a"] = set()

dict_set["a"].add(1)
dict_set["a"].add(1)

print(dict_set.items())

# Phase 2: Automate specific key with value

dict_set = {}
dict_set.setdefault("a", set()).add(2)
print(dict_set.items())

# Phase 3: Initialize any key with default value

dict_set = defaultdict(set)
dict_set["a"].add(3)
print(dict_set.items())
