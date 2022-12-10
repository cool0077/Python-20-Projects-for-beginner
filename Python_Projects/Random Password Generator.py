import string
import random

def generate_password():
    characters = list(string.ascii_letters + string.digits + "@!#$%^&*(_+")
    password_length = int(input("How long would you like your password: "))
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    
    password = "".join(password)
    print(password)
    
options = input("Do you wanna generate a password(Yes/No): ")
if options == "Yes":
    generate_password()
elif options == "No":
    print("Mabye next time")
    quit()
else:
    print("Invalid text, please try again")