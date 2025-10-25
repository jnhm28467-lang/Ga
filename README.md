# simple_directory.py
# CLI directory: username, password, name, email
# - 3 password attempts then exit
# - email view allowed but only 3 total email accesses, then exit

import sys
import getpass

# Sample in-memory directory. In real apps, do NOT store plaintext passwords.
DIRECTORY = {
    "ahmed": {"password": "pass123", "name": "Ahmed Ali", "email": "ahmed@example.com"},
    "sara" : {"password": "sara!@#", "name": "Sara Kareem", "email": "sara@example.com"},
    "hussein": {"password": "hussein2025", "name": "Hussein Omar", "email": "hussein@example.com"},
}

MAX_PASSWORD_ATTEMPTS = 3
MAX_EMAIL_VIEWS = 3

def login():
    """
    Ask for username and password.
    Allow up to MAX_PASSWORD_ATTEMPTS for password for the provided username.
    If username doesn't exist, ask again (counts toward attempts).
    On three failed attempts (password or unknown user), exit the program.
    Returns the logged-in username (key in DIRECTORY) on success.
    """
    attempts = 0
    while attempts < MAX_PASSWORD_ATTEMPTS:
        username = input("Username: ").strip()
        # Use getpass so password not shown in terminals
        password = getpass.getpass("Password: ")
        attempts += 1

        user = DIRECTORY.get(username)
        if user and password == user["password"]:
            print(f"\nWelcome, {user['name']}! You are logged in as '{username}'.\n")
            return username
        else:
            remaining = MAX_PASSWORD_ATTEMPTS - attempts
            print("Invalid username or password.", end=" ")
            if remaining > 0:
                print(f"Try again ({remaining} attempts left).\n")
            else:
                print("\nMaximum attempts reached. Closing directory.")
                sys.exit(0)

def main():
    print("=== Simple Directory CLI ===")
    print(f"Note: After {MAX_PASSWORD_ATTEMPTS} failed password attempts the directory will close.")
    print(f"Also: The email can be accessed only {MAX_EMAIL_VIEWS} times in total across all users.\n")

    email_views = 0

    while True:
        print("Options:")
        print("  1) Login")
        print("  2) List usernames")
        print("  3) Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            username = login()
            # logged-in menu
            while True:
                print("Logged-in options:")
                print("  a) View my name")
                print("  b) View my email (counts toward global email view limit)")
                print("  c) Logout")
                sub = input("Choose (a/b/c): ").strip().lower()

                if sub == "a":
                    print(f"Name: {DIRECTORY[username]['name']}\n")

                elif sub == "b":
                    if email_views >= MAX_EMAIL_VIEWS:
                        print("Email access limit reached. Closing directory now.")
                        sys.exit(0)
                    email_views += 1
                    print(f"Email: {DIRECTORY[username]['email']}")
                    print(f"(Email viewed {email_views} / {MAX_EMAIL_VIEWS} times total.)\n")
                    if email_views >= MAX_EMAIL_VIEWS:
                        print("Email access limit reached. Closing directory now.")
                        sys.exit(0)

                elif sub == "c":
                    print(f"Logged out {username}.\n")
                    break

                else:
                    print("Unknown option.\n")

        elif choice == "2":
            print("Usernames in directory:")
            for u in DIRECTORY.keys():
                print(" -", u)
            print()

        elif choice == "3":
            print("Exiting. Bye.")
            sys.exit(0)

        else:
            print("Invalid choice.\n")

if name == "main":
    main()
