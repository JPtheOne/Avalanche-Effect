import os 
from AES import*
from RC4 import*
from Analysis import*

current_dir = os.path.dirname(os.path.abspath(__file__))
rawDocs_folder = os.path.join(current_dir, 'Raw Docs')
print(rawDocs_folder)
eDocs_folder = os.path.join(current_dir,"Encrypted Docs")
dDocs_folder = os.path.join(current_dir,"Decrypted Docs")

print(current_dir)
'''
str_key = "LLAVE ULTRA SECRETA DE SEGURIDAD"
key_256bits = generate_Key(str_key)
print("Input key: ", key_256bits)
'''

for doc in os.listdir(rawDocs_folder):
    doc_path = os.path.join(rawDocs_folder, doc)
    aes_encrypt_file(doc_path, eDocs_folder)
