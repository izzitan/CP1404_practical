try:
    numerator = int(input("Enter the numerator: "))
    while True:
        denominator = int(input("Enter the denominator: "))
        if denominator != 0:
            break
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
Q1 When will a ValueError occur?
    If the input is not a number
Q2 When will a ZeroDivisionError occur?
    If the input of denominator is 0
Q3 Could you change the code to avoid the possibility of a ZeroDivisionError?
"""