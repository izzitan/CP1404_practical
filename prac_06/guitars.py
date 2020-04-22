"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

from prac_06.guitar import Guitar

count = 0
guitars = []
print("My guitars!")

name = input("Name: ")
while name != "":
    year = input("Year: ")
    cost = input("Cost: ")
    guitars.append(Guitar(name, year, cost))
    print("Guitar", count + 1, guitars[count], "added.")
    count += 1
    name = input("Name: ")


#guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
#guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("These are my guitars:")

for i, guitar in enumerate(guitars):
    print("Guitar {}: {:>20} ({}), worth ${:10} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, guitar.is_vintage()))