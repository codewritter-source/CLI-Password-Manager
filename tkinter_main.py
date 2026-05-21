


import tkinter as tk
from master_password import *
from storage import *
from generator import *

from tkinter import messagebox, simpledialog




create_master_menu = """
Create a Master Password: \n
    1. Generate a master password
    2. Manually create a master password
    3. Exit
            """


def main():
    main_option = 0
    num = simpledialog.askinteger("Main Menu", """
Main Menu: \n
    1. Add an entry
    2. Get an entry
    3. Delete an entry
    4. Create master password
    5. Exit
        """
                            )
    main_option += num
    if main_option == 1:
        entry_option = 0
        entry_factor = simpledialog.askinteger("Create an Entry",  """
Create an entry: \n
    1. Generate a password for the entry
    2. Assign a password for the entry

            """
                                )
        entry_option += entry_factor
        if entry_option == 1:
            add_generated_entry(generate())
        elif entry_option == 2:
            add_entry()



    root = tk.Tk()
    root.mainloop()

main()
