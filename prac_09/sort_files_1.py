"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""
import shutil
import os

def main():
    print(os.getcwd())

    os.chdir('FilesToSort')

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')
        try:
            os.mkdir(extension[1])
        except FileExistsError:
            pass
        try:
            shutil.move(filename, extension[1])
        except shutil.Error:
            pass


if __name__ == '__main__':
    main()