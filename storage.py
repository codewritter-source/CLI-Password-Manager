


from encryption import encrypt, decrypt
from key import key
from main import main

import csv


def add_entry ():
    while True:
#       Receive entry
        account = input("Enter service provider: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
#       Encrypt data
        encrypted_username = encrypt(username, key)
        encrypted_password = encrypt(password, key)

        save(account, encrypted_username, encrypted_password)

        decision = input("Do you wish to add another entry? (y/n): ")
        if decision.strip().lower() == "y":
            continue
        elif decision.strip().lower() == "n":
            main()

def add_generated_entry (password):
    account = input("Enter service provider: ")
    username = input("Enter your username: ")
    password = password.strip()

#   Encrypt entry
    encrypted_username = encrypt(username, key)
    encrypted_password = encrypt(password, key)

#   Save entry
    save(account, encrypted_username, encrypted_password)

    print("Password has been created. The entry has been saved successfully.")
    main()

def get_entry ():
    search = input("Enter a tag to search database: ")
    with open('password.csv', 'r', encoding = 'utf-8') as file:
        lines = file.read().splitlines()
    found = False

#   Search database for entry
    for line in lines:
        account, encrypted_username, encrypted_password = line.split(",")
        username = decrypt(encrypted_username.strip(), key)
        password = decrypt(encrypted_password.strip(), key)
        account = account.strip()

        if search == account:
            print(
                f"""
Found an entry for: {account}
    Username: {username}
    Password: {password}
                """
            )
            found = True
            break

    if not found:
        print('No entry found with this tag. \n')
        main()

def save (account, encrypted_username, encrypted_password):
    with open('password.csv','a', encoding = 'utf-8') as file:
#       Save data
        file.write(f"{account},{encrypted_username},{encrypted_password} \n")


def delete_entry ():
    print(
        """
WARNING: Removing an entry will permanently delete it from the database. This action cannot be undone.
        """
    )

    account_to_delete = input("Enter the title of the entry you want to delete: ")

#   Confirmation Phrase
    message = 'I want to delete'
    print(f"Write '{message}' in the line below to continue.")
    text = input("Write the message here: ")
    if text != message:
        print("The message you entered is not correct.")
        main()

    with open('password.csv', 'r', newline = "") as file:
        rows = list(csv.reader(file))

#   Keep only the rows that don't match the tag.
    keep = []
    for row in rows:
        if row[0] != account_to_delete:
            keep.append(row)

#   Write the filtered rows back to the file.
    with open('password.csv', 'w', newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(keep)

    print(f" Entry of tag '{account_to_delete}' has been successfully removed.")



