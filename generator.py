


# Random password generation function. It returns a randomly selected string
# with 15 to 26 characters (user option) of numbers, letters and symbols.
# add_generated_entry() function in 'storage.py'


import string, random

def generate ():
    letter_upper = string.ascii_letters.upper()
    letter_lower = string.ascii_letters.lower()
    number = string.digits
    symbol = string.punctuation
    chars = letter_upper + letter_lower + number + symbol
    length = int(input("Enter the length of the password (15-26): "))

#   Generate password
    password = ""
    for space in range(0, length):
        password += random.choice(chars)
    return password


