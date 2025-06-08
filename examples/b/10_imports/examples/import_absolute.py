# Example: Absolute imports
import asyncio

# Enforce absolute imports
from __future__ import absolute_import

# Absolute imports
from product.api.submodule1 import func1
from product.core.submodule2 import func2
from product.gui.submodule3 import func3

# Call all functions
func1()
func2()
func3()
