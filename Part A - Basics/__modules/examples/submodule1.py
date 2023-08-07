""" Enabling the absolute import future will allow to write safer Py2 code by disabling relative imports.

In the example if the future is not enabled the interpreter will take the package found by scanning the standard
library directories and then the current directory. If the future is enabled the import will be only accepted
by specifying explicitly the location of the module.

Requirements: Use Py2 as project interpreter
"""

from __future__ import absolute_import
import submodule3
submodule3.a = 2

print(submodule3.a)