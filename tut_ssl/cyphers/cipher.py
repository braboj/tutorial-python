from cryptography.fernet import Fernet

if __name__ == "__main__":
    key = Fernet.generate_key()
    print(key)

    data = b"Hello world!"
    f = Fernet(key)
    ciphertext = f.encrypt(data)
    print(ciphertext)

    plaintext = f.decrypt(ciphertext)
    print(plaintext)