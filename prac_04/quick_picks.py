"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""
import random

CONSTANTS = []


def main():
    quick_pick = int((input("How many quick picks? ")))
    random_numbers = []
    for line in range(quick_pick):
        random_numbers = []
        for i in range(6):
            random_numbers.append(generate_random_number())
        print(sorted(random_numbers))


def generate_random_number():
    while True:
        random_number = random.randint(1, 45)
        if random_number in CONSTANTS:
            pass
        else:
            CONSTANTS.append(random_number)
            return random_number


main()
