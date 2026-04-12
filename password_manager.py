


import sys

def add_entry():
    while True:
        tag = input("Enter a title for this entry: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        save(tag, username, password)

        decision = input("Do you wish to add another entry? (y/n): ")
        if decision.strip().lower() == "y":
            continue
        elif decision.strip().lower() == "n":
            main()

def get_entry():
    search = input("Enter a tag to search database: ")
    with open('password.csv', 'r', encoding = 'utf-8') as file:
        lines = file.read().splitlines()
    found = False

    for line in lines:
        tag, username, password = line.split(",")
        tag = tag.strip()
        username = username.strip()
        password = password.strip()

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
        print('No entry found with this tag.')

def save(tag, username, password):
    with open('password.csv','a', encoding = 'utf-8') as file:
        file.write(f"{tag},{username},{password} \n")

def close_program():
    decision = input("Are you sure you wish to exit? (y/n): ")
    if decision.strip().lower() == "y":
        sys.exit()

def main():
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
        add_entry()
    elif option == 2:
        get_entry()
    elif option == 3:
        close_program()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
