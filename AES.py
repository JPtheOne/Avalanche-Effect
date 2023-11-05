import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt_file(input_file_path, key=None):
    # Generate a new key if one is not provided
    if not key:
        key = get_random_bytes(32)  # A 256-bit key

    cipher = AES.new(key, AES.MODE_CBC)
    
    # Read the contents of the file
    with open(input_file_path, 'rb') as f:
        plaintext = f.read()

    # Encrypt the content
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    # Create the encrypted file path
    encrypted_file_path = os.path.join(
        os.path.dirname(input_file_path),
        "AES-EN" + os.path.basename(input_file_path)
    )

    # Write the IV and the encrypted content to the output file
    with open(encrypted_file_path, 'wb') as f:
        f.write(cipher.iv)
        f.write(ciphertext)
    
    cipherbits = ''.join(format(byte, '08b') for byte in ciphertext)


    # Return the key and the path of the encrypted file
    return key, cipherbits

def aes_decrypt_file(encrypted_file_path, key):
    # Read the IV and the ciphertext from the file
    with open(encrypted_file_path, 'rb') as f:
        iv = f.read(16)  # AES block size is 16 bytes
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    # Create the decrypted file path
    decrypted_file_path = os.path.join(
        os.path.dirname(encrypted_file_path),
        "AES.Decrypted_" + os.path.basename(encrypted_file_path).replace("AES.Encrypted_", "", 1)
    )

    # Write the decrypted content to the output file
    with open(decrypted_file_path, 'wb') as f:
        f.write(plaintext)

    # Return the path of the decrypted file
    return decrypted_file_path

#aes_decrypt_file("Docs/Aes.Encrypted_doc2.pdf", key= b'SuperSecureOriginalKeyforAES2023')