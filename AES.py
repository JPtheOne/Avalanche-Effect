import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt_file(filename, output_folder, key=None):
    if not key:
        key = get_random_bytes(32)  

    cipher = AES.new(key, AES.MODE_CBC)
    with open(filename, 'rb') as f:
        plaintext = f.read()

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    base_name = os.path.basename(filename)
    encrypted_base_name = "Encrypted_" + base_name

    output_filename = os.path.join(output_folder, encrypted_base_name)    

    with open(output_filename, 'wb') as f:
        f.write(cipher.iv)
        f.write(ciphertext)


def aes_decrypt_file(filename, output_folder, key):
    with open(filename, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    base_name = os.path.basename(filename)
    decrypted_base_name = base_name.replace("Encrypted_", "Decrypted_")

    output_filename = os.path.join(output_folder, decrypted_base_name)

    with open(output_filename, 'wb') as f:
        f.write(plaintext)

#aes_encrypt_file("/Raw Docs/Act7.docx")
