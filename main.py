import os 
from AES import*
from RC4 import*
from Analysis import*

guinea_pig = 'Docs/doc1.docx'

#1. AE for Only AES

str_or_key_AES=generate_Key('SuperSecureOriginalKeyforAES2023')
or_key_AES = int(str_or_key_AES,2).to_bytes(32,byteorder='big')
print(f"AES key: {(or_key_AES)}")

str_mod_key_AES, mod_key_AES = modify_Key(or_key_AES)
print(f"Modded AES key: {str_mod_key_AES}")


key1,cipherbits1= aes_encrypt_file(guinea_pig, or_key_AES)
key2, cipherbits2 = aes_encrypt_file(guinea_pig, mod_key_AES)

onlyAES_AE = avalanche_effect(cipherbits1,cipherbits2)
print(f"AE score: {onlyAES_AE:.2f}% for {guinea_pig[5:]}")


# 2. AE for Only RC4
str_or_key_RC4 = generate_Key('SuperSecureOriginalKeyforRC42023')
or_key_RC4 = int(str_or_key_RC4,2).to_bytes(32,byteorder='big')
print(f"RC4 key: {or_key_RC4}")

str_mod_key_RC4, mod_key_RC4 = modify_Key(or_key_RC4)
print(f"Modded AES key: {str_mod_key_RC4}")

key1, cipherbits3 = rc4_encrypt_file(guinea_pig, or_key_RC4)
key2, cipherbits4 = rc4_encrypt_file(guinea_pig, mod_key_RC4)

onlyRC4_AE = avalanche_effect(cipherbits3,cipherbits4)
print(f"AE score: {onlyRC4_AE:.2f}% for {guinea_pig[5:]}")



# 3. RC4-AES
# First encrypt with RC4
RC4_key,rc4_cipheredText=rc4_encrypt_file(guinea_pig, or_key_RC4)

#Obtain output path of RC4
rc4_encrypted_file_basename = "RC4-EN" + os.path.basename(guinea_pig)
rc4_encrypted_file_path = os.path.join(os.path.dirname(guinea_pig), rc4_encrypted_file_basename)

#Encrypt RC4 output with AES
AES_key, ciphertext1 =aes_encrypt_file("Docs/RC4-ENdoc2.pdf", or_key_AES)

#Repeat same steps but now with other keys
mod_rc4_key, mod_rc4_ciphered_bits = rc4_encrypt_file(guinea_pig, mod_key_RC4)
mod_rc4_encrypted_file_basename = "RC4-EN" + os.path.basename(guinea_pig)
mod_rc4_encrypted_file_path = os.path.join(os.path.dirname(guinea_pig), mod_rc4_encrypted_file_basename)
mod_aes_key, ciphertext2 = aes_encrypt_file(mod_rc4_encrypted_file_path, mod_key_AES)

# Return AE for this RC4+AES
rc4_and_aes_AE = avalanche_effect(ciphertext1,ciphertext2)
print(f"AE score: {rc4_and_aes_AE:.2f}% for RC4 and AES for {guinea_pig[5:]}")

# 4. Proposed (AES + RC4)
aes_encrypted_file_basename = "AES-EN" + os.path.basename(guinea_pig)
aes_encrypted_file_path = os.path.join(os.path.dirname(guinea_pig), aes_encrypted_file_basename)

aes_key, aes_cipheredText = aes_encrypt_file(guinea_pig, or_key_AES)

rc4_key, ciphertext1 = rc4_encrypt_file(aes_encrypted_file_path, or_key_RC4)

mod_aes_key, mod_aes_cipheredText = aes_encrypt_file(guinea_pig, mod_key_AES)

mod_rc4_key, ciphertext2 = rc4_encrypt_file(aes_encrypted_file_path, mod_key_RC4)

aes_and_rc4_AE = avalanche_effect(ciphertext1, ciphertext2)
print(f"AE score: {aes_and_rc4_AE:.2f}% for AES and RC4 for {os.path.basename(guinea_pig)}")


