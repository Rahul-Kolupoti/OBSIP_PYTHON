import string
import random

Char_len=int(input("Enter length of the password:"))
char_types=input("Enter character types to use(letters - 1, numbers - 2, symbols - 3)):")

pwd=""

for x in char_types:
    if x=='1':
        pwd+=string.ascii_letters
    elif x=='2':
        pwd+=string.digits
    elif x=='3':
        pwd+=string.punctuation

password = ''.join(random.choice(pwd) for _ in range(Char_len))

print(password)