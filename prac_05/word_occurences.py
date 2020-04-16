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
    sorted_dict = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)
    i = 0
    for word in sorted_dict:
        print("""{:<10}:  {:>3}""".format(*word))
        i += 1
    dictionary = {}
    text = input("Text: ")

