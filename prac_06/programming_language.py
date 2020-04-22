"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""


class ProgrammingLanguage:
    """Represents a programming language object """

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Construct or initialise a ProgrammingLanguage object with parameters passed in"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)