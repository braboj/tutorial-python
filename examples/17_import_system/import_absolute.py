# Shows how to enforce and use absolute imports.
# ------------------------------------------------------------------------------
# Example script demonstrating absolute imports.
# Using absolute imports
import asyncio

# Enforce absolute imports
from __future__ import absolute_import

# Absolute imports
from foo.api.submodule1 import func1
from foo.core.submodule2 import func2
from foo.gui.submodule3 import func3

# Call all functions
func1()
func2()
func3()
