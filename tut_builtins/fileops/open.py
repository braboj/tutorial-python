"""
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

file - path-like object (representing a file system path)
mode - (optional) - mode while opening a file. If not provided, it defaults to 'r' (open for reading in text mode).
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)

buffering (optional) - used for setting buffering policy
encoding (optional) - the encoding format
errors (optional) - string specifying how to handle encoding/decoding errors
newline​ (optional) - how newlines mode works (available values: None, ' ', '\n', 'r', and '\r\n'
closefd (optional) - must be True (default); if given otherwise, an exception will be raised
opener (optional) - a custom opener; must return an open file descriptor
"""

f = open("test.txt", mode="w", encoding='utf-8')
f.writelines("Hello world")
f.close()

f = open("test.txt", mode="r", encoding='utf-8')
print(f.readline())
