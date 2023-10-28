from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes

def rc4_encrypt_file(filename, output_filename, key=None):
    if not key:
        key = get_random_bytes(16)  # Key length for RC4 can vary, but 16 bytes is a common choice.

    cipher = ARC4.new(key)
    with open(filename, 'rb') as f:
        plaintext = f.read()

    ciphertext = cipher.encrypt(plaintext)
    with open(output_filename, 'wb') as f:
        f.write(ciphertext)

    return key

def rc4_decrypt_file(filename, output_filename, key):
    with open(filename, 'rb') as f:
        ciphertext = f.read()

    cipher = ARC4.new(key)
    plaintext = cipher.decrypt(ciphertext)
    with open(output_filename, 'wb') as f:
        f.write(plaintext)


