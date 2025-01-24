from cryptography.fernet import Fernet
import os 

###########################
#THIS CORRELATES TO WHERE 
#THE KEY IS STORED, IT MUST
#BE STORED ENCRYPTED
###########################


def get_or_make_key():
    key_path = 'fernet_key.key' 
    if(os.path.exists(key_path)):
        #key already exists
        with open(key_path, 'rb') as file:
            enc_key = file.read()
            # print("Key loaded successfully.")
        #key doesnt exist
    else:
        enc_key = Fernet.generate_key()
        with open(key_path, "wb") as file:
            file.write(enc_key)
        # print("Key generated and saved successsfully")
    return enc_key

def encrypt_password(plaintxt_pw):
    enc_key = get_or_make_key()
    cipher_suite = Fernet(enc_key)
    encrypted_pw = cipher_suite.encrypt(plaintxt_pw.encode())#encode string to bytes before encrypting
    return encrypted_pw

def decrypt_password(encrypted_pw):
    enc_key = get_or_make_key()
    cipher_suite = Fernet(enc_key)
    decrypted_pw = cipher_suite.decrypt(encrypted_pw)
    return decrypted_pw.decode('utf-8')    