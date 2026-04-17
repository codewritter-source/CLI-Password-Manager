## CLI-Password-Manager 

A simple command‑line password manager built for learning purposes.
This project demonstrates how to generate, store, and verify a master password using salted hashing, and how to manage passwords securely in a local vault.

⚠️ Security Notice  
This project uses SHA‑256 + salt for password hashing.
While this is acceptable for educational purposes, it is not secure enough for real‑world password storage.
Modern password managers use slow, memory‑hard algorithms like Argon2, bcrypt, or PBKDF2 to resist brute‑force attacks.

🚀 Features

🔐 Master Password System -
Create your own master password or generate a random one.
Salted SHA‑256 hashing for basic verification.
Stored in master.txt as <salt_hex>:<hash_hex>.

🗄️ Password Vault -
Store credentials in a local CSV file (master.csv).
Add, view, and manage entries through a CLI menu.

🎲 Random Password Generator -
Uses a custom generator module to create strong random passwords.

🧩 Modular Code Structure -
Separate modules for generation, verification, encryption, storage and menu logic,
so that alternative updates can be integrated (AES, Argon2, cloud storage)
Avoids circular imports and keeps logic clean.

CLI-PasswordManager/

─ generator.py          - Random password generator

─ master_passsword.py   - Master password creation & verification

─ menu.py               - Main menu logic

─ key.py                - Symmetric Cipher key for testing

─ encryption.py         - Stores Cipher Encryption logic

─ main.py               - Entry point of the application

─ master.txt            - Stored salt + hash (created at runtime)

─ password.csv          - Password vault (created at runtime)

─ README.md             - Project documentation

🛠️ Installation

git clone https://github.com/codewritter-source/CLI-PasswordManager

📜 License

This project is released under the MIT License.
Feel free to modify, learn from, and build upon it.

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Open a pull request or start a discussion in the Issues tab.
