"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
Count the occurences of words in a string
"""

dictionary = {}
count = 0

text = input("Text: ")
while text != "":
    for word in text.split():
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1
        count += 1
    for word in dictionary:
        print("""{}:  {}""".format(word, dictionary[word]))
    dictionary = {}
    text = input("Text: ")

