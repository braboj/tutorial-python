from api.submodule1 import *
from core.submodule2 import *
from comp.submodule3 import *

# Namespace api.submodule1
func1()
print(f"Module {func1.__module__} my_id set to {func1.__globals__['my_id']}")
print()

# Namespace core.submodule2
func2()
print(f"Module {func2.__module__} my_id set to {func2.__globals__['my_id']}")
print()

# Namespace comp.submodule3
func3()
print(f"Module {func3.__module__} my_id set to {func3.__globals__['my_id']}")
print()