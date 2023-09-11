# Example of the export decorator that shall be placed in the __init__.py file of the package

# Export decorator
def export(defn):
    # Add the object to the global namespace
    globals()[defn.__name__] = defn

    # Set the object to be exported
    __all__.append(defn.__name__)

    # Return the object
    return defn


# Example of the export decorator
@export
def func4():
    print('func4')