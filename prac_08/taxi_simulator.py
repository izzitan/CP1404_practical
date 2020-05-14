"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_fare = 0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>>")
        if choice.lower() == "c":
            print("Taxis avaliable:")
            count = 0
            for taxi in taxis:
                print("{} - {}".format(count, taxi))
                count += 1
            taxi_choice = input("Choose Taxi: ")
            current_taxi = taxis[int(taxi_choice)]
            print("Bill to date: ${:.2f}".format(total_fare))

        elif choice.lower() == "d":
            distance = input("Drive how far? ")
            current_taxi.start_fare()
            current_taxi.drive(int(distance))
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            total_fare += current_taxi.get_fare()
            print("Bill to date: ${:.2f}".format(total_fare))

        elif choice.lower() == "q":
            print("Total trip cost: ${:.2f}".format(total_fare))
            print("Taxis are now:")
            count = 0
            for taxi in taxis:
                print("{} - {}".format(count, taxi))
                count += 1
            break



main()
