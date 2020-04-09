"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""
import random

NUMBERS = []
NUMBERS_OF_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    quick_pick = int((input("How many quick picks? ")))
    for line in range(quick_pick):
        random_numbers = []
        for i in range(NUMBERS_OF_LINE):
            random_numbers.append(generate_random_number())
        print(sorted(random_numbers))


def generate_random_number():
    while True:
        random_number = random.randint(MINIMUM, MAXIMUM)
        if random_number in NUMBERS:
            pass
        else:
            NUMBERS.append(random_number)
            return random_number


main()
