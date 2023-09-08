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
