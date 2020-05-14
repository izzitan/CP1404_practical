"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

from prac_08.unreliable_car import UnreliableCar

def main():
    car = UnreliableCar("Car 1", 100, 50)
    car.drive(50)
    print(car)
    car.drive(50)
    print(car)


main()
