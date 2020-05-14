"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Silver Service", 100, 2)
    taxi.start_fare()
    taxi.drive(18)
    print(taxi)
    print("Total fare is: ${:.2f}".format(taxi.get_fare()))


main()
