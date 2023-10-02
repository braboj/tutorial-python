import namespace_pkg
print(namespace_pkg.__path__)

from namespace_pkg import plugin
print(plugin.__path__)