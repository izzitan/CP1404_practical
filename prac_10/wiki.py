"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

import wikipedia


def main():
    key = input("Search a wikipedia page: ")
    while key != "":
        try:
            wiki = wikipedia.page(key)
            print(wiki.title)
            print(wiki.url)
            print(wiki.summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        key = input("Search a wikipedia page: ")


if __name__ == '__main__':
    main()
