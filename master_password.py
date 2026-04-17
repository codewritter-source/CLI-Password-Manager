


"""
WARNING: SHA‑256 with a salt is not sufficient for secure password storage.
         Fast hashes like SHA‑256 are vulnerable to brute‑force attacks.
         It is purely educational and not intended to store secure information.

"""


import hashlib
import os
import sys

from generator import generate


def generate_master():
    # Master password is generated randomly.
    master_password = generate()
    confirmation = input(f"This is the master password {master_password}: \n WARNING : If you forget this password, you will permanently \
                        lose access to the vault. \n Are you sure you want this password? (y/n): ")

    # Create a random 16-byte salt.
    if confirmation.strip() == 'y':
        salt = os.urandom(16)

        # Combine salt + password (as bytes) and compute SHA-256.
        hash_obj = hashlib.sha256(salt + master_password.encode())
        password_hash = hash_obj.hexdigest()

        # Store salt and hash in the format: <salt_hex>:<hash_hex>
        stored_hash = salt.hex() + ':' + password_hash
        with open("master.txt", "w") as master_file:
            master_file.write(stored_hash)
    else:
        create_master()


def create_master():
    master_password = input("Please enter the master password: ")
    confirmation = input(f"This is the master password {master_password}: \n WARNING : If you forget this password, you will permanently \
                                lose access to the vault. \n Are you sure you want this password? (y/n): ")

    # Create a salt.
    if confirmation.strip() == 'y':
        salt = os.urandom(16)

        # Combine salt + password (as bytes) and compute SHA-256.
        hash_obj = hashlib.sha256(salt + master_password.encode())
        password_hash = hash_obj.hexdigest()

        # Store salt and hash in the format: <salt_hex>:<hash_hex>
        stored_hash = salt.hex() + ':' + password_hash
        with open("master.txt", "w") as master_file:
            master_file.write(stored_hash)

        sys.exit()

def verify_master():
    master_password = input("Please enter the master password: ")

    # Load hash value.
    with (open("master.txt", "r") as master_file):
        hashed_value = str(master_file.read().strip())

        # Extract salt and stored hash from the file.
        salt_hex, stored_hash = hashed_value.split(':')
        salt = bytes.fromhex(salt_hex)

        # Recompute SHA‑256(salt + entered_password) to verify.
        hash_obj = hashlib.sha256(salt + master_password.encode())
        input_hash = hash_obj.hexdigest()

        # Compare computed hash with stored hash
        if input_hash == stored_hash:
            return True
        else:
            return False




