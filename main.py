


from master_password import *
from storage import *
from generator import *
import os, sys



def main():
    if os.path.exists("master.txt"):
        confirmed = verify_master()
        if confirmed:
            main_menu()
        else:
            close_program()
    else:
        main_menu()


def close_program():
    decision = input("Are you sure you wish to exit? (y/n): ")
    if decision.strip().lower() == "y":
        sys.exit()

def main_menu():
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
CREATE MASTER PASSWORD:
    1. Generate a password for the entry
    2. Assign a password for the entry

            """
        )

        entry_option = int(input("Choose an option: "))
        if entry_option == 1:
            add_generated_entry(generate())
        elif entry_option == 2:
            add_entry()

    elif option == 2:
        get_entry()
    elif option == 3:
        delete_entry()
    elif option == 4:
        if os.path.exists("master.txt"):
            print("Sorry,master password already exists.")
        else:
            print(
                """
Create a Master Password:
    1. Generate a master password
    2. Manually create a master password
    3. Exit
                """
            )
        master_option = int(input("Choose an option: "))
        if master_option == 1:
            generate_master()
        elif master_option == 2:
            create_master()
        elif master_option == 3:
            close_program()

    elif option == 5:
        close_program()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()