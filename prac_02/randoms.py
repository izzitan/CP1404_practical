import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
Q1 What was the smallest number you could have seen, what was the largest?:
    Smallest = 5, largest = 20
Q2 What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
    Smallest = 3, largest = 10, No
Q3 What was the smallest number you could have seen, what was the largest?
    Smallest = 2.5, largest = 5.5
"""

print(random.randint(1,100))