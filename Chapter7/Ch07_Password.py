#importing regex module
import re


def checkPassword(password):

    password_regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
    mo = password_regex.search(password)

    if mo is None:
        print(password, 'is not a valid password')
    else:
        print(password, 'is a valid password')

password_input = input('Enter the password to be checked - ')
checkPassword(password_input)
