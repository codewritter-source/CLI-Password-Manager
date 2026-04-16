import os

from storage import get_entry, add_entry, add_generated_entry, delete_entry
from generator import generate
from master_password import verify_master, generate_master, create_master
import sys


def close_program():
    decision = input("Are you sure you wish to exit? (y/n): ")
    if decision.strip().lower() == "y":
        sys.exit()

def menu():
    #   Menu is getting out of hand. Options: dictionary menu.
    print(
        """"
Main Menu: \n
    1. Add an entry
    2. Get an entry
    3. Delete an entry
    4. Create master password
    5. Exit
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
        delete_entry()
    elif option == 4:
        if os.path.exists("master.csv"):
            print("Master password already exists.")
        else:
            print(
                """
Create a Master Password:
    1. Generate a master password
    2. Manually create a master password
    3. Return
                """
            )
        if option == 1:
            generate_master()
        elif option == 2:
            create_master()
        elif option == 3:
            menu()

    elif option == 5:
        close_program()
    else:
        print("Invalid option.")

def main():
    if os.path.exists("master.csv"):
        verify_master()
    else:
        menu()

if __name__ == "__main__":
    main()