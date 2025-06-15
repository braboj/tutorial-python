# data_defaultdict

```python
# Automatic keys with defaultdict
# -----------------------------------------------------------------------------
# defaultdict automatically creates missing keys so your code doesn't need explicit checks.

from collections import defaultdict


def test_default_factory(factory):

    d = defaultdict(factory)

    # Test the defaultdict
    try:
        print(d['key1'])
        print(d['key2'])
        print(d['key3'])

    except KeyError as e:
        print("KeyError: {}".format(e))
        assert True

    print()


if __name__ == "__main__":

    default_factories = [
        None,               # Behaves like a regular dictionary
        str,                # Returns an empty string if the key is not found
        int,                # Returns 0 if the key is not found
        float,              # Returns 0.0 if the key is not found
        list,               # Returns an empty list if the key is not found
        tuple,              # Returns an empty tuple if the key is not found
        dict,               # Returns an empty dictionary if the key is not found
        set,                # Returns an empty set if the key is not found
        lambda: 'value',    # Returns a default value if the key is not found
    ]

    for default_factory in default_factories:
        test_default_factory(default_factory)
```
