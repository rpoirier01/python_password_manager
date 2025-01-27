import secrets 
import string
from zxcvbn import zxcvbn

#TODO ADD COMMAND
def gen_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(int(length)):
        password+=secrets.choice(chars)
    # print(password)
    return password

def check_pw_strth(pw):
    pw_strth = zxcvbn(pw)
    # print(f"Score: {pw_strth['score']}, Feedback: {pw_strth['feedback']}")
    if(pw_strth['score']<=2):
        print("This password is not very secure, here are some suggestions to improve it:")
        for sgs in pw_strth['feedback']['suggestions']:
            print('\t' + sgs)
        print("Alternatively, you can generate a secure password with: python main gen")
    else:
        print("This password is secure")
