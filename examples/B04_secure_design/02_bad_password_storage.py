# Password Storage - Bad Example
# ------------------------------------------------------------------------------
# Storing or hashing passwords without a salt and a strong hash function makes
# them easy to crack if the database is compromised.

import hashlib

password = input('Enter password: ')

# BAD: Unsalted, single round MD5 hash
hash_value = hashlib.md5(password.encode('utf-8')).hexdigest()
print('Storing password hash:', hash_value)
