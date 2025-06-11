"""Triggers a circular import between two submodules."""
import circular.submodule1 as submodule1

submodule1.func1()

