


# Random password generation function. It returns a randomly selected string
# with +12 characters (user option) of numbers, letters and symbols.
# add_generated_entry() function in 'storage.py'

import string as text
import random


def generate():
#   text = string module
    letter_upper = text.ascii_letters.upper()
    letter_lower = text.ascii_letters.lower()
    number = text.digits
    symbol = text.punctuation

    chars = letter_upper + letter_lower + number + symbol
    string = ''

    length = int(input("Enter the length of the password: "))

    if length > 12:
        for char in range(0, length):
            string += random.choice(chars)
    elif length < 12:
        raise ValueError("Password length must be greater than 12")

