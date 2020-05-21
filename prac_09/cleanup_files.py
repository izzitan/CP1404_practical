"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""

    new_name = ""
    for current_index, current_letter in enumerate(filename):
        new_name = new_name + current_letter
        if current_index < len(filename) - 1:
            if current_letter.isalnum() and filename[current_index+1].isupper():
                new_name += "_"
    new_name = new_name.replace(" ", "_").replace(".TXT", ".txt").replace(".T_X_T", ".txt")
    return new_name


main()