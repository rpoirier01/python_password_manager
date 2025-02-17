import getpass
from bcrypt import hashpw, gensalt, checkpw
from database import get_master_pw_hash, set_master_pw_hash, add_website_credentials, read_credentials_by_name_website, update_credentials, delete_credential, read_all_credentials, make_password_table, build_master_password_table
from encryption import encrypt_password, decrypt_password
from pw_operations import gen_password, check_pw_strth
from splunk import master_password_error_log, successful_master_login_log, new_password_added_log, user_added_insecure_pw_log, user_updated_insecure_pw_log, user_updated_secure_pw_log

def initial_setup():
    build_master_password_table()
    master_pw_hash_list = get_master_pw_hash()
    make_password_table()
    if(not (master_pw_hash_list == [])):
        master_pw_hash = master_pw_hash_list[0]
        while(True): #alternative implentation of a do-while loop
            entered_pw = getpass.getpass("Please enter master password to unlock password manager: ")
            if(checkpw(entered_pw.encode(), master_pw_hash)):
                print("Correct password entered, access granted!")
                successful_master_login_log()
                break
            else:
                print("Incorrect password entered, try again")
                master_password_error_log()

    else:
        print("Before using the program, a master password must be set")
        master_pw_unhashed = getpass.getpass("Please enter a new master password: ")
        hashed_pw = hashpw(master_pw_unhashed.encode(), gensalt())#salt the hash to prevent rainbow table attacks
        set_master_pw_hash(hashed_pw)


def print_options():
    # options = input("Would you like to create a new password(C), read a password(R) update an existing password(U), delete a password(D)?(C/R/U/D or full word or exit)\n")
    options = input('''
Would you like to create a new password(C), read a password(R), update a password(U), delete a password(D), generate a new secure password(G) or check the security of passwords(CH)?(C/R/U/D/G/CH or full word or exit)
''')
    return options.lower()

def add_new_password():
    print("To add a new password, a username, password and website are required")
    username = input("Please enter username:\n")
    password, secure = _take_password_input()
    
    website = input("Please enter the website:\n")
    if(username == None or password == None or website == None):
        print("Error, username, password and website cannot be left empty")
        return
    enc_pw = encrypt_password(password)
    try:
        add_website_credentials(username, enc_pw, website)
        print("Successfully added new credentials!")
        if(secure):
            new_password_added_log(username, website)
        else:
            user_added_insecure_pw_log(username, website)
    except:
        print("Error: This record already exists, the combination of username and website MUST be unique (but you can have multiple unique usernames for the same website)")

def _take_password_input():
    password = None
    password2 = ''
    while(True):#Alternate do while
        password = getpass.getpass("Please enter new password:\n")
        password2 = getpass.getpass("Please re-enter password:\n")
        if(password == password2 and password != ''):
            break
        print("Please enter the same password twice (passwords cannot be 0 characters)")
    print('-------------------')
    is_secure = check_pw_strth(password)
    print('-------------------')
    return password, is_secure

def read_password():
    print("To read a password, a username and website is required")
    username = input("Please enter a username or type ALL for all password records:\n")
    if(username.lower()=="all"):
        records = read_all_credentials()
        for record in records:
            print("*********************")
            print("Website: " + record[0])
            print("Username: " + record[1])
            print("Password: " + decrypt_password(record[2]))
        print("*********************")   
        return  
        
    website = input("Please enter a website name:\n")
    if(username == None or website == None):
        print("Username and website cannot be left empty")
        return
    credentials = read_credentials_by_name_website(username, website)
    if(credentials == None):
        print("Error no credentials found with that website and username")
        return
    password = decrypt_password(credentials[2])
    print("Credentials for this site:\nwebsite: " + credentials[0] + "\nUsername: " + credentials[1] +  "\nPassword: " + str(password))
    # print("Credentials for that site are: \n" + str(credentials))

def update_password():
    print("To update credentials, a username and website for the original password are required along with new credentials")
    original_username = input("Please enter the current username:\n")
    original_website = input("Please enter the current website name:\n")
    new_username = input("Please enter the new username:\n")
    new_password, new_pass_secure = _take_password_input()
    new_website = input("Please enter the new website:\n")
    if(original_username == "" or original_website == "" or new_password == "" or new_username == "" or new_website == ""):
        print("No field can be left empty!")
        return
    enc_password = encrypt_password(new_password)
    try:
        if(update_credentials(original_username, original_website, new_username, enc_password, new_website)==0):
            print("Error: no values found with that username/website combination")
            return
        else:
            if(new_pass_secure):
                user_updated_secure_pw_log(new_username, new_website)
            else:
                user_added_insecure_pw_log(new_username, new_website)
            print("Successfully updated value")
    except:
        print("Error: cannot records with identical username/website combinations")
    

def delete_record():
    print("To update credentials, a username and website are required")
    username = input("Please enter username:\n")
    website = input("Please enter website:\n")
    if(username == None or website == None):
        print("Username and website required")
        return
    if(delete_credential(username, website)==0):
        print("Error, no values found with that username/website combination")
        return
    else:
        print("Successfully deleted record")

def generate_secure_password():
    length = input("Please enter a length for your secure password \n(8 characters is the minimum recommended, but longer is better)\n")
    if(length==0):
        print("Error, length of password cannot be 0")
        return
    print(gen_password(length))

def check_all_pw_strth():
    credentials = read_all_credentials()
    #website, username, password
    for c in credentials:
        print(f"*************************\nUsername is {c[1]} and website is {c[0]}")
        check_pw_strth(decrypt_password(c[2].decode()))
    print("*************************")

