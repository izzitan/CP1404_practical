"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_data(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    parts_list = []

    input_file = open(FILENAME)
    for line in input_file:
        """
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        """

        line = line.strip()
        parts = line.split(",")
        parts[2] = int(parts[2])
        parts_list.append(parts)

    input_file.close()
    return parts_list

def print_data(data):
    for item in data:
        print("{} is taught by {} and has {} students".format(*item))


main()
