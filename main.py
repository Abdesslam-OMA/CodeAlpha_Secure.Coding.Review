
import sqlite3
import hashlib
import os

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

connection.commit()


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    
    query = f"""
    INSERT INTO users (username, password)
    VALUES ('{username}', '{hashed_password}')
    """

    cursor.execute(query)
    connection.commit()

    print("User registered successfully!")



def login():
    username = input("Username: ")
    password = input("Password: ")

    query = f"""
    SELECT * FROM users
    WHERE username = '{username}'
    """

    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        if hashed_password == user[2]:
            print("Login successful!")
            print("Welcome", username)
        else:
            print("Incorrect password!")
    else:
        print("User not found!")


# Admin function
def admin_panel():
    print("\nWelcome to the Admin Panel!")
    print("1. View database")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        for user in users:
            print(user)


while True:
    print("\n===== LOGIN SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Admin Panel")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        admin_panel()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
