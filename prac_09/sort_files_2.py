"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""
import shutil
import os


def main():
    print(os.getcwd())

    os.chdir('FilesToSort')

    extensions = {}

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')
        extensions.update({extension[1]: None})

    for extension in extensions:
        folder = input("What category would you like to sort {} files into? ".format(extension))
        extensions[extension] = folder
        try:
            os.mkdir(folder)
        except FileExistsError:
            pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        name, extension = filename.split('.')
        print(extensions[extension])
        try:
            shutil.move(filename, extensions[extension])
        except shutil.Error:
            pass


if __name__ == '__main__':
    main()
