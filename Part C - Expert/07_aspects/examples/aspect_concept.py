# -*- coding: utf-8 -*-
import re

from six import with_metaclass


class Aspecter(type):
    aspect_rules = []
    wrapped_methods = []

    def __new__(cls, name, bases, dict):

        # Iterate over all methods and wrap them
        for key, value in dict.items():

            # If the method is callable and not the metaclass
            if hasattr(value, "__call__") and key != "__metaclass__":
                # Wrap the method
                dict[key] = Aspecter.wrap_method(value)

        # Get the new class
        aspecter = type.__new__(cls, name, bases, dict)

        # Return the new class
        return aspecter

    @classmethod
    def register(cls, name_pattern="", in_objects=(), out_objects=(),
                 pre_function=None, post_function=None):

        rule = {
            "name_pattern": name_pattern,  # Regular expression for method names
            "in_objects": in_objects,  # ???
            "out_objects": out_objects,  # ???
            "pre": pre_function,  # Junstion point before method call
            "post": post_function  # Junstion point after method call
        }

        cls.aspect_rules.append(rule)

    @classmethod
    def wrap_method(cls, method):

        # Wrap the method
        def call(*args, **kw):

            # Get the pre functions
            pre_functions = cls.match_pre_functions(method, args, kw)

            # Call the pre functions
            for function in pre_functions:
                function(*args, **kw)

            # Call the method
            results = method(*args, **kw)

            # Get the post functions
            post_functions = cls.match_post_functions(method, results)

            # Call the post functions
            for function in post_functions:
                function(results, *args, **kw)

            # Return the results from the original method
            return results

        # Return the wrapped method
        return call

    @classmethod
    def match_names(cls, method):
        # Return the matching names for the methods
        return [rule for rule in cls.aspect_rules
                if re.match(rule["name_pattern"], method.__name__)
                or rule["name_pattern"] == ""
                ]

    @classmethod
    def match_pre_functions(cls, method, args, kw):

        # Get all the arguments for the method
        all_args = args + tuple(kw.values())

        # This is a fukcing mess (not readable, not maintainable)
        return [rule["pre"] for rule in cls.match_names(method)
                if rule["pre"] and
                (rule["in_objects"] == () or
                 any((type(arg) in rule["in_objects"] for arg in all_args)))
                ]

    @classmethod
    def match_post_functions(cls, method, results):

        # Convert the results to a tuple
        if type(results) != tuple:
            results = (results,)

        # This is a fukcing mess (not readable, not maintainable)
        return [
            rule["post"] for rule in cls.match_names(method)
            if rule["post"] and (
                    rule["out_objects"] == () or
                    any((type(result) in rule["out_objects"] for result in results))
            )
        ]


class Address(object):
    def __repr__(self):
        return "Address..."


class Person(with_metaclass(Aspecter)):

    def update_address(self, address: Address):
        print("Updating address to {}".format(address))

    def __str__(self):
        return "person object"


def log_update(*args, **kwargs):
    print("Logging on update of {}".format(str(args[0])))


def log_address(*args, **kwargs):
    print("Logging on address update")
    addresses = [arg for arg in (args + tuple(kwargs.values()))
                 if type(arg) == Address]
    print(addresses)


if __name__ == "__main__":
    Aspecter.register(name_pattern="^update.*", pre_function=log_update)
    Aspecter.register(in_objects=(Address,), pre_function=log_address)

    p = Person()
    p.update_address(Address())
