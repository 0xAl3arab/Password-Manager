from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import json
import os
import ast

masterpassword = "password123"
salt = os.urandom(16)
iv = os.urandom(16)
kdf = Scrypt(salt , 32,2**14,8,1)

key = kdf.derive(masterpassword.encode())

cipher = Cipher(algorithms.AES(key) , modes.CBC(iv))

def encrypt_and_store(data_dict):
    json_data = json.dumps(data_dict)  

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(json_data.encode()) + padder.finalize()

    encryptor = cipher.encryptor()
    
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
   




    
    with open("data.txt" ,"w") as f:
        f.writelines(str(ciphertext))
        



users = {
    "alice": "password123",
    "bob": "qwerty456",
    "charlie": "letmein789",
    "diana": "testpass000"
}
encrypt_and_store(users)



with open("data.txt" , "r") as f:
    encrypted_data = ast.literal_eval(f.readlines()[0])
    print(type(encrypted_data))
    


decryptor = cipher.decryptor()
decrypted_bytes = decryptor.update(encrypted_data) + decryptor.finalize()
#print(decrypted_bytes)

unpadder = padding.PKCS7(128).unpadder()
decrypted = unpadder.update(decrypted_bytes) + unpadder.finalize()

real_data = decrypted.decode()
print(real_data)
