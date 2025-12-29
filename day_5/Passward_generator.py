logo = """
========================================
        🔐 PASSWORD GENERATOR 🔐
========================================

        ┌───────────────┐
        │  ***********  │
        │  ***********  │
        │  ***********  │
        └───────────────┘
              ||
        🔒 Secure • Random • Strong

----------------------------------------
"""
print(logo)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_input = int(input("how many letters you want in your password 1,2,3,4... : "))
numbers_input = int(input("how many numbers you want in your password 1,2,3,4... : "))
symbols_input = int(input("how many symbols you want in your password 1,2,3,4... : "))


# For easy password

password = ""

for char in range(0,letters_input):
    password += random.choice(letters)

for char in range(0,numbers_input):
    password += random.choice(numbers)

for char in range(0,symbols_input):
    password += random.choice(symbols)

print(password)


# For hard password 

# use of shuffle 

password_list = list(password)
random.shuffle(password_list)
# password = "".join(password_list) (easy way and short code to shuffle)

#Other way to shuffle list

password = ""
for char in password_list :
     password += char
print(f"Your password is : {password}")
