namespace = globals()

abstracts = set(name for name, value in namespace.items() if getattr(value, "__isabstractmethod__", False))
print(abstracts)