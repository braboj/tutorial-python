""" Hash module

Converts data of arbitrary length to data of fixed length. The fixed size data is also called a digest. Hashes are
used to used to check passwords without storing them...

Scenario:

An application must verify the password given by an user in the code. The password can be stored in plaintext
somewhere but then the program will be vulnerable to attacks. The solution is to store it in an obfuscated form
which will be compared to the obfuscated user input. If both are the same then the password is the same.

Hashes are also used to verify that data is not manipulated when using secure communication. The encrypted data is
hashed and send along with the data. The receiver hashes the encryped data on its side and compares it with the
received digest. If both differ then someone tried to manipulate the data.

Hashes are very sensitive to changes. Chaning even one bit can trigger a change in the digest of big magnitude.
Choosing the most secure hash function is crucial to ensure that the data is safe.

Salting is also important when two or more users have the same passwords. Adding different randomized salts to each
password helps to make each unique. For example, if your password is iL0veCh3ese! and another user, Chioma,
has that exact password, salting is used to make those password hashes unique.

Hashing is also used to guarantee uniqueness of the elements in data classes. For example keys in dictionaries use
hashes to guarantee uniqueness.

Features:
 - Unique fixed size output
 - Same input gives the same output

Usecases:
 - Protect against tempering
 - Store passwords
 - Use as identificator for files or in data structures

Algorithms:
md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(),
sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256.

https://en.wikipedia.org/wiki/Hash_function
https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/
https://cheapsslsecurity.com/blog/decoded-examples-of-how-hashing-algorithms-work/

"""
import random
import string
from hashlib import md5, sha256


def hash_string(string):

    # Define the hash algorithm
    my_hash = md5()

    # Add string before hashing. Each call concatenates the string.
    my_hash.update(string.encode('utf-8'))

    # Return digest as bytes
    digest_dec = my_hash.digest()

    # Return digest as hex string
    digest_hex = my_hash.hexdigest()

    return digest_hex


if __name__ == "__main__":

    ##########################################################################
    # Usecase 1: Comparing passwords
    stored_password = hash_string('password')
    user_input = hash_string('password')
    print(stored_password, user_input)
    if stored_password == user_input:
        print('Password is valid')

    ##########################################################################
    # Usecase 2: Protection against tempering
    data_sent = "hello"
    digest_sent = hash_string(data_sent)

    data_received = 'hellu'
    digest_check = hash_string(data_received)

    print(digest_sent, digest_check)
    if digest_sent != digest_check:
        print('Somebody manipulated the data')

    ##########################################################################
    # Usecase 3: Use salt to ensure no two hashes are the same

    user1 = 'password'
    salt1 = random.choice(string.ascii_letters)

    user2 = 'password'
    salt2 = random.choice(string.ascii_letters)

    # Store the digests and the salts in a database
    # The salt is only known to the verifier
    digest1 = hash_string(user1 + salt1)
    digest2 = hash_string(user2 + salt2)

    print(digest1, digest2)
    # Now two users with the same passwords have different digests
    if digest1 != digest2:
        print("Two users with the same password have different digests")


