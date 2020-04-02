#Task One
name = input("Please enter your name: ")
name_file = open("name.txt", "w")
print(name, file=name_file)
name_file.close()

#Task Two
read_name_file = open("name.txt", "r")
print("Your name is {}".format(read_name_file.readline()))
read_name_file.close()

#Task Three
number_file = open("numbers.txt", "r")
number1 = int(number_file.readline())
number2 = int(number_file.readline())
print("Sum of two numbers is {}".format(number1 + number2))
number_file.close()

#Task Four
number_file = open("numbers.txt", "r")
numbers = [int(line) for line in number_file.readlines()]
print("Sum of all numbers is {}".format(sum(numbers)))
number_file.close()
