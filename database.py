import sqlite3

def build_master_password_table():
    connection = sqlite3.connect('password_manager.db')
    cursor = connection.cursor()

    #Master PW table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS master_password (
        id INTEGER PRIMARY KEY,
        hashed_password BLOB NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

def make_password_table():
    #PW table 
    connection = sqlite3.connect('password_manager.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS credentials (
        website TEXT NOT NULL,
        username TEXT NOT NULL,
        password BLOB NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (website, username)
    )
    ''')
    connection.commit()
    connection.close()


def get_master_pw_hash():
    connection = sqlite3.connect('password_manager.db')
    cursor = connection.cursor()
    cursor.execute("SELECT hashed_password FROM master_password")
    return cursor.fetchone()

def set_master_pw_hash(hashed_master_password):
    connection = sqlite3.connect('password_manager.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO master_password (id, hashed_password) values (? , ?)
    ''', ('1', hashed_master_password))
    connection.commit()
    connection.close()

def add_website_credentials(username, encrypted_pw, website):
    with sqlite3.connect('password_manager.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO credentials (website, username, password) values (?, ?, ?)
        ''', (website, username, encrypted_pw))


def read_credentials_by_name_website(username, website):
    with sqlite3.connect('password_manager.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT website, username, password, created_at FROM credentials WHERE website = ? AND username = ?
        ''', (website, username))
        credential = cursor.fetchone()
    return credential

def read_all_credentials():
    with sqlite3.connect('password_manager.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT website, username, password FROM credentials ''')
        all_results = cursor.fetchall()
    return all_results

def update_credentials(old_username, old_website, new_username, new_password, new_website):
    with sqlite3.connect('password_manager.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE credentials
            SET website=?, username=?, password=?
            WHERE website=? AND username=?
        ''', (new_website, new_username, new_password, old_website, old_username))
        result = cursor.rowcount #return the number of rows affected
    return result

def delete_credential(username, website):
    with sqlite3.connect('password_manager.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM credentials WHERE website = ? AND username = ?", (website, username))
        number_deleted = cursor.rowcount
    return number_deleted