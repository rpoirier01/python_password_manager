import pytest
from encryption import encrypt_password, decrypt_password
from database import add_website_credentials, read_all_credentials, delete_credential, update_credentials, read_credentials_by_name_website

def test_encrypt_decrypt():
    assert(decrypt_password(encrypt_password("Test String"))=="Test String") #ensure encrypting, decrypting is equal to the original
    encrypt_password('') #test empty string cases



def test_database_add_unique():
    starting_records = len(read_all_credentials())
    add_website_credentials("Unique Username", "Password", "Unique Website")
    ending_records = len(read_all_credentials())
    delete_credential("Unique Username", "Unique Website")
    assert(starting_records+1 == ending_records)

def test_database_add_repeat():
    starting_records = len(read_all_credentials())
    add_website_credentials("Unique Username", "Password", "Unique Website")
    try:
        add_website_credentials("Unique Username", "Password", "Unique Website")
    except:
        print("Repeated record error")
    ending_records = len(read_all_credentials())
    delete_credential("Unique Username", "Unique Website")
    assert(starting_records+1 == ending_records) #only 1 record should be added
    
def test_database_update_repeat():
    add_website_credentials("Unique Username", "Password", "Unique Website")
    add_website_credentials("Second Unique Username", "Password", "Unique Website")
    try:
        update_credentials("Second Unique Username", "Unique Website", "Unique Username", "Password", "Unique Website")
    except:
        print("Repeated record error")
    records = read_all_credentials()
    delete_credential("Unique Username", "Unique Website")
    delete_credential("Second Unique Username", "Unique Website")
    assert(True == (("Unique Website", "Unique Username", "Password")in records) == (("Unique Website", "Second Unique Username", "Password" ) in records))

def test_database_update_not_found():
    assert(0==update_credentials("Second Unique Username", "Unique Website", "Unique Username", "Password", "Unique Website"))# this record should NOT be found in the table, and shouldnt throw an error

def test_delete_not_found():
    assert(0==delete_credential("Second Unique Username", "Unique Website"))#this record should not exist in the table

def test_delete_found():#deleting a single added record should result in the same number of records
    starting_records = len(read_all_credentials())
    add_website_credentials("Unique Username", "Password", "Unique Website")
    delete_credential("Unique Username", "Unique Website")
    assert(starting_records == len(read_all_credentials()))

def test_get_one_record_found():
    add_website_credentials("Unique Username", "Password", "Unique Website")
    record = read_credentials_by_name_website("Unique Username", "Unique Website")
    delete_credential("Unique Username", "Unique Website")
    for field in ("Unique Website", "Unique Username", "Password"): #get 1 record includes when the record was created, so this is necessary
        assert field in record

def test_get_one_record_unfound():
    record = read_credentials_by_name_website("Unique Username", "Unique Website")
    assert(record==None)