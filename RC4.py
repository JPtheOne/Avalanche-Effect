import os
from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes

def rc4_encrypt_file(filename, key=None):
    if not key:
        key = get_random_bytes(32)  # Key length for RC4 can vary, but 16 bytes is a common choice.

    cipher = ARC4.new(key)
    with open(filename, 'rb') as f:
        plaintext = f.read()

    ciphertext = cipher.encrypt(plaintext)

     # Prepare the output file path with "RC4-E" prefix
    encrypted_file_path = os.path.join(
        os.path.dirname(filename),
        "RC4-EN" + os.path.basename(filename)
    )

    with open(encrypted_file_path, 'wb') as f:
        f.write(ciphertext)
    
    cipherbits = ''.join(format(byte, '08b') for byte in ciphertext)

    return key, cipherbits

def rc4_decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as f:
        ciphertext = f.read()

    cipher = ARC4.new(key)
    plaintext = cipher.decrypt(ciphertext)
    
    decrypted_file_path = os.path.join(
        os.path.dirname(encrypted_file_path),
        "RC4-Decrypted_" + os.path.basename(encrypted_file_path).replace("RC4-EN", "", 1)
    )


    with open(decrypted_file_path, 'wb') as f:
        f.write(plaintext)




#key = rc4_encrypt_file("AES.Encrypted_doc1.docx")
#print(key)
#key =b'\x93\xf8\x19\xcd8\xc8\xbc\xd8:KF\xa5dm[Y'
#rc4_decrypt_file("RC4-EAES.Encrypted_doc1.docx",key)