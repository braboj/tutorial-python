# Password Storage - Good Example
# ------------------------------------------------------------------------------
# Use a strong key derivation function with a unique salt for each password.
# PBKDF2 is built into Python's hashlib module.

import os
import hashlib
import base64

password = input('Enter password: ')

salt = os.urandom(16)
hash_bytes = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)

encoded_salt = base64.b64encode(salt).decode('utf-8')
encoded_hash = base64.b64encode(hash_bytes).decode('utf-8')

print('Storing password hash:')
print(f'salt={encoded_salt}')
print(f'hash={encoded_hash}')
