"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""


def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = get_name(email)
        while True:
            name_check = input("Is your name {}? (Y/n)".format(name))
            if name_check.lower() == "n":
                name = input("Name: ")
                break
            if name_check.lower() == "y":
                break
        email_to_name.update({name: email})
        email = input("Email: ")

    for (key, value) in email_to_name.items():
        print("{} ({})".format(key, value))


def get_name(email):
    email_name = email.split("@")
    name_title = email_name[0].title()
    name_list = name_title.split(".")
    name = " ".join(name_list)
    return name


main()
