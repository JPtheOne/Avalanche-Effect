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




