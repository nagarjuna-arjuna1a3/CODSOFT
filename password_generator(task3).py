import random
import string
length = int(input("enter the password length"))
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
all_characters = letters + digits +symbols
password = ""
for i in range(length):
    password += random.choice(all_characters) 
print(" generated password:",password)