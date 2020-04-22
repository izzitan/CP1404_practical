"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(gibson)

another_guitar = Guitar("Another Guiter", 2013, 1000)
print(another_guitar)

print("{} get_age() - Expected 98. Got {}".format(gibson.name, gibson.get_age()))
print("{} get_age() - Expected 7. Got {}".format(another_guitar.name, another_guitar.get_age()))
print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))
print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))