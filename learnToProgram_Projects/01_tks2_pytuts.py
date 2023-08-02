# ask a user to Enter a calculatin: 5 * 7
# print out 5 * 7 = 35
# Store the user input of 2 numbers and the operator
# convert the strings into integers

# if "+", then we need to provide output based on addition
# print the result


num1, operator, num2 = input('Enter Calculations: ').split()
# the split method will separate the users input on each character space

num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num2 + num1))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num2 * num1))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
    print("{} % {} = {}".format(num1, num2, num1 % num2))
else:
    print("basic arithmetric only, try again")
