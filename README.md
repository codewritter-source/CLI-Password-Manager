## CLI-Password-Manager 


When the master password feature was added, it caused a circular dependency between 'master_password.py' and 'main.py'.

Tried to seperate menu from 'main.py' to a 'menu.py'. It fixed that circular dependency but created another between 'menu.py' and 'master_password.py'.

Options: OOP
