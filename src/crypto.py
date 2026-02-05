from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import json

def generate_initialization_vector():
    init_vector = os.urandom(16)
    return init_vector

def generate_salt():
    salt = os.urandom(16)
    return salt

def derive_key(password , salt):
    assert(len(salt)==16),"salt size should be 16 bytes"
    # convert password from text to bytes
    password_bytes = password.encode()
    #creating the key derivation function object
    kdf = Scrypt(salt , 32 , 2**14 , 8 , 1)
    #deriving the key using Scrypt
    key = kdf.derive(password_bytes)

    return key

def encrypt_data(data , key , init_vector):
    #convert data from json to bytes
    data_bytes = data.encode()

    try :
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data_bytes) + padder.finalize()
    except Exception as e:
        print("padding failed")

    try :

        cipher = Cipher(algorithms.AES(key) , modes.CBC(init_vector))
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    except Exception as e:
        print("encryption failed")

    return encrypted_data 

def decrypt_data(encrypted_data , key ,init_vector):
    try :
        cipher = Cipher(algorithms.AES(key) , modes.CBC(init_vector))

        decryptor = cipher.decryptor()

        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    except Exception as e:
        print("decryption failed")

    return decrypted_data.decode()

#test case
key = derive_key("mypassword123" , b'\tp\xcf\xc7\x18\xbei$\xea\xf5\x0ea\xcb\xbd_\t')
salt = b'\tp\xcf\xc7\x18\xbei$\xea\xf5\x0ea\xcb\xbd_\t'
init_vector = b'\xf0?\x0b\xff)\xf1\xaf\xdc\xc4\xde\xf1\xed\x12\x08:\xe9'

users = {
    "alice": "password123",
    "bob": "qwerty456",
    "charlie": "letmein789",
    "diana": "testpass000"
}
users_json = json.dumps(users)
data = encrypt_data(users_json ,key , init_vector )

#tested successfully , still need to parse data .
print(decrypt_data(data , key , init_vector))









