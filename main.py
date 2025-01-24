from cli_operations import initial_setup, print_options, add_new_password, read_password, update_password, delete_record
from database import read_all_credentials, read_credentials_by_name_website
import sys
initial_setup()


while True:
    option = print_options()

    if(option.lower() =="create" or option.lower()=='c'):
        add_new_password()
    elif(option.lower()=="read" or option.lower()=='r'):
        read_password()
    elif(option.lower()=="update" or option.lower()=='u'):
        update_password()
        # print(read_all_credentials())
    elif(option.lower()=="delete" or option.lower()=='d'):
        delete_record()
    elif(option.lower()=="exit"):
        print("Exiting program")
        sys.exit()
    else:
        print("Please enter a valid option")
