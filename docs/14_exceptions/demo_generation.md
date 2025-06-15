# demo_generation

```python
# Old-Style Exception Generation
# --------------------------------------------------------------------------------
# Shows what happens when raising an exception class that does not inherit from
# BaseException.

# class NewStyleException(Exception): pass
#
# try:
#    raise NewStyleException
# except BaseException:
#     print("Caught")


class OldStyleException: pass

try:
   raise OldStyleException
# except BaseException:
#     print("BaseException caught when raising OldStyleException")
except:
   print("Caught")
```
