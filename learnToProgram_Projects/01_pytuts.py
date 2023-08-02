# Ask the user to input 2 values and store them in variable num1 and num2
num1, num2 = input("Please enter two nubers ").split()

# convert the strings into regular numbers Integer
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
sum = num1 + num2

# Subtract values and store in difference
difference = num1 - num2

# Multiply the values and store in product
product = num2 * num1

# Divide the values and Store in qoutient
qoutient = num1 / num2

# Use modulus on the values to find the remainder
remainder = num1 % num2

# Print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, qoutient))
print("{} % {} = {}".format(num1, num2, remainder))
