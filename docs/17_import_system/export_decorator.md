# export_decorator

```python
# Defines an export decorator for populating a package's __all__.
# ------------------------------------------------------------------------------
# Utility that adds functions to a package's __all__.
# Demonstrates placing the export decorator in a package's __init__ file

# Export decorator
def export(defn):
    # Add the object to the global namespace
    globals()[defn.__name__] = defn

    # Set the object to be exported
    __all__.append(defn.__name__)

    # Return the object
    return defn


# Demonstration of the export decorator
@export
def func4():
    print('func4')
```
