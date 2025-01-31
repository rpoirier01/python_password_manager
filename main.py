from cli_operations import initial_setup, print_options, add_new_password, read_password, update_password, delete_record, generate_secure_password, check_all_pw_strth
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
    elif(option.lower()=="delete" or option.lower()=='d'):
        delete_record()
    elif(option.lower()=="gen" or option.lower()=="generate" or option.lower()=='g'):
        generate_secure_password()
    elif(option.lower()=='check' or option.lower()=='ch'):
        check_all_pw_strth()
    elif(option.lower()=="exit" or option.lower()=='e'):
        print("Exiting program")
        sys.exit()
    else:
        print("Please enter a valid option")
