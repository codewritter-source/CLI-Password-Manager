


import string, random


#   add_generated_entry() function in 'storage.py'

def generate ():
    letter = string.ascii_letters
    number = string.digits
    symbol = string.punctuation
    chars = letter + number + symbol
    length = int(input("Enter the length of the password (15-26): "))

#   Generate password
    password = ""
    for space in range(0, length):
        password += random.choice(chars)
    return password

