# data_base64

```python
# Base64 encoding
# -----------------------------------------------------------------------------
# Base64 converts binary data to ASCII text. This is handy when transmitting bytes over text-based protocols.

import base64

# Convert the string to bytes
text_expected = 'Здравейте, хора!'
text_stream = text_expected.encode('utf-8')

# Encode the byte stream in Base64
encoded = base64.b64encode(text_stream)
print(encoded)

# Decode the byte stream from Base64
decoded = base64.b64decode(encoded)

# Print the decoded string
text_obtained = decoded.decode('utf-8')
print(text_obtained)

# Assert that the expected and obtained strings are equal
assert text_expected == text_obtained
```
