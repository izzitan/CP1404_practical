"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(
                                                             self.name,
                                                             self.current_fare_distance,
                                                             self.price_per_km,
                                                             self.flagfall)
