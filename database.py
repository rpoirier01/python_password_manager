import sqlite3


connection = sqlite3.connect('password_manager.db')
cursor = connection.cursor()

#Master PW table
cursor.execute('''
CREATE TABLE IF NOT EXISTS master_password (
    id INTEGER PRIMARY KEY,
    hashed_password BLOB NOT NULL
)
''')

#PW table 
cursor.execute('''
CREATE TABLE IF NOT EXISTS credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password BLOB NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
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
    connection = sqlite3.connect('password_manager.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO credentials (website, username, password) values (?, ?, ?)
    ''', (website, username, encrypted_pw))
    connection.commit()
    connection.close()

def read_credentials_by_name_website(username, website):
    connection = sqlite3.connect('password_manager.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT website, username, password, created_at FROM credentials WHERE website = ? AND username = ?
    ''', (website, username))
    return cursor.fetchone()

def read_all_credentials():
    connection = sqlite3.connect('password_manager.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT website, username, password FROM credentials ''')
    return cursor.fetchall()

def update_credentials(old_username, old_website, new_username, new_password, new_website):
    connection = sqlite3.connect('password_manager.db')
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE credentials
        SET website=?, username=?, password=?
        WHERE website=? AND username=?
    ''', (new_website, new_username, new_password, old_website, old_username))
    connection.commit()
    return cursor.rowcount #return the number of rows affected

def delete_credential(username, website):
    connection = sqlite3.connect('password_manager.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM credentials WHERE website = ? AND username = ?", (website, username))
    connection.commit()
    return cursor.rowcount