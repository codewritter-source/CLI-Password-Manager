


from encryption import encrypt, decrypt
from key import key
import sys
import random, string


def add_entry ():
    while True:
        tag = input("Enter a title for this entry: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        encrypted_username = encrypt(username, key)
        encrypted_password = encrypt(password, key)
        save(tag, encrypted_username, encrypted_password)

        decision = input("Do you wish to add another entry? (y/n): ")
        if decision.strip().lower() == "y":
            continue
        elif decision.strip().lower() == "n":
            main()

def get_entry ():
    search = input("Enter a tag to search database: ")
    with open('password.csv', 'r', encoding = 'utf-8') as file:
        lines = file.read().splitlines()
    found = False

    for line in lines:
        tag, encrypted_username, encrypted_password = line.split(",")
        username = decrypt(encrypted_username.strip(), key)
        password = decrypt(encrypted_password.strip(), key)
        tag = tag.strip()


        if search == tag:
            print(
                f"""
Found an entry for: {tag}
    Username: {username}
    Password: {password}
                """
            )
            found = True
            break

    if not found:
        print('No entry found with this tag. \n')
        main()

def save (tag, encrypted_username, encrypted_password):
    with open('password.csv','a', encoding = 'utf-8') as file:
        file.write(f"{tag},{encrypted_username},{encrypted_password} \n")

def close_program( ):
    decision = input("Are you sure you wish to exit? (y/n): ")
    if decision.strip().lower() == "y":
        sys.exit()

def generate ():
    letter = string.ascii_letters
    number = string.digits
    symbol = string.punctuation
    chars = letter + number + symbol

    password = ""
    for space in range(0, 26):
        password += random.choice(chars)
    return password

def add_generated_entry (password):
    tag = input("Enter a title for this entry: ")
    username = input("Enter your username: ")
    encrypted_username = encrypt(username, key)
    password = password.strip()
    encrypted_password = encrypt(password, key)

    save(tag, encrypted_username, encrypted_password)

    print("Password has been created. The entry has been saved successfully.")
    main()

def main ():
    print(
        """"
Main Menu: \n
    1. Add an entry
    2. Get an entry
    3. Exit
        """
    )

    option = int(input("Choose an option: "))
    if option == 1:
        print(
            """
ADD AN ENTRY:
    1. Generate a password for the entry
    2. Assign a password for the entry
    3. Return
            
            """
        )

        entry_option = int(input("Choose an option: "))
        if entry_option == 1:
            add_generated_entry(generate())
        elif entry_option == 2:
            add_entry()
        elif entry_option == 3:
            main()

    elif option == 2:
        get_entry()
    elif option == 3:
        close_program()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
