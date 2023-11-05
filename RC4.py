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
    
    # The naming here should mirror how the encrypted file is named during the encryption process
    decrypted_file_path = os.path.join(
        os.path.dirname(encrypted_file_path),
        "RC4-Decrypted_" + os.path.basename(encrypted_file_path).replace("RC4-EN", "", 1)
    )

    with open(decrypted_file_path, 'wb') as f:
        f.write(plaintext)

    return decrypted_file_path  # Make sure this return statement is correctly aligned and not within any loop or conditional.



    with open(decrypted_file_path, 'wb') as f:
        f.write(plaintext)


#rc4_encrypt_file("Docs/AES-ENdoc1.docx", key=b'SuperSecureOriginalKeyforRC42023')
rc4_decrypt_file("Docs/RC4-ENAES-ENdoc1.docx", key=b'SuperSecureOriginalKeyforRC42023')