"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
Dictionary to convert colours to hex code
"""

COLOUR_TO_HEX = {
    "aquamarine": "#7fffd4",
    "cyan": "#00ffff",
    "coral": "#ff7f50",
    "gold": "#ffd700",
    "navyblue": "#000080",
    "orchid": "#da70d6",
    "pink": "#ffc0cb0",
    "purple": "#a020f0",
    "violet": "#ee82ee",
    "brown": "#a52a2a"
}

print(COLOUR_TO_HEX)

colour = input("Enter colour name: ")
while colour != "":
    if colour.lower() in COLOUR_TO_HEX:
        print(colour.lower(), "is", COLOUR_TO_HEX[colour.lower()])
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ")