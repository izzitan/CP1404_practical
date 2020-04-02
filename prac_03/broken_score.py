"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

import random

def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)
    print(get_result(random.randint(0, 100)))

def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif 50 <= score < 90:
        return "Passable"
    elif 90 <= score <= 100:
        return "Excellent"
    elif 50 > score >= 0:
        return "Bad"


main()
