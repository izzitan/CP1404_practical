"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""


def main():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number: ")))
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_valid = False
    username = input("Please input your username: ")
    for user in usernames:
        if username == user:
            user_valid = True
    if user_valid:
        print("Access granted")
    else:
        print("Access denied")


main()
