"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

while True:
    sales = float(input("Enter sales: $"))
    if 0 < sales < 1000:
        bonus = sales * 0.1
        print("Bonus is {:.2f}".format(bonus))
    elif sales >= 1000:
        bonus = sales * 0.15
        print("Bonus is {:.2f}".format(bonus))
    elif sales < 0:
        print("Thank you")
        break
    else:
        print("Invalid input")

