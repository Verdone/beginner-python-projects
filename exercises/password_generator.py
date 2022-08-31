from ast import Pass
from secrets import choice
import string, random

chars = list(string.ascii_letters + string.digits + string.punctuation)

def make_password():

    password_length = int(input("> Length of password to be generated: \n> "))
    if 1 < password_length < 25:
        pass
    else:
        print("Input not accepted, restart application to try again.")
        quit()

    random.shuffle(chars)
    password = []

    for x in range(password_length):
        password.append(random.choice(chars))
    
    random.shuffle(password)
    password = "".join(password)

    print("> Generated password is ", password)

choice = input("> Create a password between 1 and 25 characters? (Y/n) \n> ")
yes = {'Yes', 'yes', 'Y', 'y'}
no = {'No', 'no', 'N', 'n'}

if choice in yes:
    make_password()
elif choice in no:
    print("> Program ended. Restart application to make a password.")
    quit()
else:
    print("Input not accepted, restart application to try again.")
    quit()