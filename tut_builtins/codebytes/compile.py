# coding: utf-8
"""
The compile() method returns a Python code object from the source (normal string, a byte string, or an AST object).

compile() method is used if the Python code is in string form or is an AST object, and you want to change it to a
code object. The code object returned by compile() method can later be called using methods like: exec() and eval()
which will execute dynamically generated Python code.

compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

Parameters:
@source - a normal string, a byte string, or an AST object

@filename - file from which the code was read. If it wasn't read from a file, you can give a name yourself

@mode - Either exec or eval or single. eval - accepts only a single expression, exec - It can take a code block that
has Python statements, class and functions, and so on and single - if it consists of a single interactive statement

@flags (optional) and dont_inherit (optional) - controls which future statements affect the compilation of the
source. Default Value: 0

@optimize (optional) - optimization level of the compiler. Default value -1.

"""

code_string = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
code_object = compile(code_string, 'sumstring', 'exec')

exec(code_object)
