# Example custom module with variables and functions
# ------------------------------------------------------------------------------
# Modules are Python files that can define variables, functions and classes.
# They allow code to be organized into reusable components. When a module is
# imported, its top-level code executes once.

PI = 3.14159


def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}"


def area_circle(radius):
    """Return the area of a circle with the given radius."""
    return PI * radius * radius


if __name__ == '__main__':
    # Code executed only when running this module directly
    print(greet('module'))
    print('Area:', area_circle(2))
