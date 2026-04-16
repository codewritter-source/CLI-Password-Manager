


"""
WARNING: SHA-256 with a salt is not sufficient for secure password storage. Fast hashes like SHA-256 are vulnerable to brute-force attacks.
         It is purely educational and it is not intended to store any secure information
"""


import hashlib, os
from generator import generate


def generate_master():
    master_password = generate()
    confirmation = input(f"This is the master password {master_password}: \n WARNING : If you forget this password, you will permanently \
                        lose access to the vault. \n Are you sure you want this password? (y/n): ")

    if confirmation.strip() == 'y':
        salt = os.urandom(16)

        # Translate master to bytes + salt.
        hash_obj = hashlib.sha256(salt + master_password.encode())
        password_hash = hash_obj.hexdigest()

        # Create hash value.
        hashed_value = salt.hex() + ':' + password_hash
        with open("master.txt", "w") as master_file:
            master_file.write(hashed_value)
    else:
        create_master()


def create_master():
    master_password = input("Please enter the master password: ")
    confirmation = input(f"This is the master password {master_password}: \n WARNING : If you forget this password, you will permanently \
                                lose access to the vault. \n Are you sure you want this password? (y/n): ")
    if confirmation.strip() == 'y':
        salt = os.urandom(16)

        # Translate master to bytes + salt
        hash_obj = hashlib.sha256(salt + master_password.encode())
        password_hash = hash_obj.hexdigest()

        # Create hash value.
        hashed_value = salt.hex() + ':' + password_hash
        with open("master.txt", "w") as master_file:
            master_file.write(hashed_value)

def verify_master():
    master_password = input("Please enter the master password: ")

    # Load hash value.
    with open("master.txt", "r") as master_file:
        hashed_value = master_file.read().strip()

        # Separate salt from master ; reformat salt for verification.
        salt_hex, password_hash = master_file.split(":")
        salt = bytes.fromhex(salt_hex)

        # Recompute hash using the same salt.
        hash_obj = hashlib.sha256(salt + master_password.encode())
        input_hash = hash_obj.hexdigest()

    if master_password == input_hash:
        menu()
    elif input_hash != hashed_value:
        main()




