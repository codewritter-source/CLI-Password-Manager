


from storage import get_entry, add_entry, add_generated_entry, delete_entry
from generator import generate

import sys


def close_program( ):
    decision = input("Are you sure you wish to exit? (y/n): ")
    if decision.strip().lower() == "y":
        sys.exit()

def main ():
#   Menu is getting out of hand. Options: dictionary menu.
    print(
        """"
Main Menu: \n
    1. Add an entry
    2. Get an entry
    3. Delete an entry
    4. Exit
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
        close_program()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
