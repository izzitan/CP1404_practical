"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

MIN_LENGTH = 4

def main():
    password = get_password()
    while not is_valid_password(password):
        print("Invalid password")
        password = get_password()
    print("Password {} is valid".format(print_asterisk(password)))

def get_password():
    password = input("Please enter your password: ")
    return password

def is_valid_password(password):
    return len(password) >= MIN_LENGTH

def print_asterisk(password):
    asterisks = ""
    for i in range(len(password)):
        asterisks = asterisks + "*"
    return asterisks


main()
