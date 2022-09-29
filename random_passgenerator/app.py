# Ask user do they need to generate the password
# if yes then generate else exit

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_pass():
    password_length = int(input("Please enter how many characters should be in your password :)"))
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
    password = "".join(password)
    return  password

print("Welcome to password generator......\n")
create_pass = input('Do you want to create a password? (y/n): ').lower().strip() == 'y'
while create_pass:
    print(generate_pass())
    create_pass = input('\nDo you want to create a new password? (y/n): ').lower().strip() == 'y'
print("Program is shutting down .....")