


# Random password generation function. It returns a randomly selected string
# with +12 characters (user option) of numbers, letters and symbols.
# add_generated_entry() function in 'storage.py'

import string as text
import random
from tkinter import messagebox, simpledialog

def generate():
#   text = string module
    letter_upper = text.ascii_letters.upper()
    letter_lower = text.ascii_letters.lower()
    number = text.digits
    symbol = text.punctuation

    chars = letter_upper + letter_lower + number + symbol
    string = ''
    sentinel = True

    while sentinel:
        length = 0
        length_factor = simpledialog.askinteger("Generate Password",
                                                "Enter the length of the password: ")

#       Generate string
        if length > 12:
            length += length_factor

            for char in range(0, length):
                string += random.choice(chars)
                confirmation = messagebox.askretrycancel("Generate Password",
                                                        f"Your password is: {string} \n Do you wish to generate a different one?")
                if confirmation == True:
                    sentinel = True
                elif confirmation == False:
                    return string










    else:
        messagebox.showerror("Error", "Password length must be greater than 12")



