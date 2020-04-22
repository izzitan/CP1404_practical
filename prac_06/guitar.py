"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""


class Guitar:
    """Represent a Guitar Object"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        return 2020 - int(self.year)

    def is_vintage(self):
        if self.get_age() > 50:
            return "(vintage)"
        else:
            return ""

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, str(self.year), str(self.cost))