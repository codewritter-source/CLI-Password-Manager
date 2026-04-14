


def encrypt(plain_text, key):
    encrypted_text = ""
    for char in plain_text:
#       Use key to encrypt text
        if char in key:
            encrypted_text += key[char]
        else:
            print(
                f""" 
WARNING: UPDATE KEY
The character '{char}' was not found in the key. '{char}' will not be encrypted, since its not in the key,
but the rest will be encrypted and the entry will be saved. 
                """
                )
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
#   Key reversed for decryption
    reverse_key = {value:key for key,value in key.items()}

    decrypted_text = ""
    for char in encrypted_text:
        if char in reverse_key:
            decrypted_text += reverse_key[char]
        else:
            print(
                f"""
WARNING: UPDATE KEY
The character '{char}' was not fount in the key. '{char}' will not be decrypted. Since it was not in the key,
it is the original character. 
                """
                )
            decrypted_text += char
    return decrypted_text



