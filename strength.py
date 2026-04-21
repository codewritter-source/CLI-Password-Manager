



import string

def strength_calculator():
    password = input("Enter your password: ")
    strength = 0
    types = 0
    length = len(password)
    upper_case_letters = 0
    numbers = 0
    symbols_list = string.punctuation
    symbols = 0

#--------------------------------------------------------------------

    # length
    if length > 16:
        strength += 2

#--------------------------------------------------------------------

    # Upper Case Letter Checkpoint (WORTH: 2 pts.)
    for char in password:
        if char.isupper():
            upper_case_letters += 1
        else:
            continue
    if upper_case_letters > 2:
        strength += 2
    if upper_case_letters > 1:
        types += 1

#--------------------------------------------------------------------

    # Digit Checkpoint (WORTH: 2 pts.)
    for char in password:
        if char.isdigit():
            numbers += 1
        else:
            continue
    if numbers > 2:
        strength += 2
    if numbers > 1:
        types += 1

#--------------------------------------------------------------------

    # Symbol Checkpoint (WORTH: 2 pts)
    for char in password:
        if char in symbols_list:
            symbols += 1
        else:
            continue
    if symbols > 2:
        strength += 2
    if symbols > 1:
        types += 1

#--------------------------------------------------------------------

    # Type Checkpoint (WORTH: 2 pts.)
    if types == 3:
        strength += 2
    elif types < 3:
        strength -= 6       # A (-6) will automatically return WEAK

#--------------------------------------------------------------------

    # Establish Categories
    if strength in range (9, 11):
        password_strength = 'VERY STRONG'
    elif strength in range(7, 9):
        password_strength = 'STRONG'
    elif strength in range(5, 7):
        password_strength = 'MEDIUM'
    elif strength < 5:
        password_strength = 'WEAK'

#---------------------------------------------------------------------

    print(f"This password is considered {password_strength}. \n Always remember to have strong and unique passwords for each provider.")



if __name__ == "__main__":
    strength_calculator()







































