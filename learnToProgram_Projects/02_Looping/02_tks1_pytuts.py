# First Task

# Have the user enter their investment amount and expectd interest
# Each year their investment will increase by their investment + their investment * interest rate
# Print out the earnings after a 10 year period


# Solution

# Ask for the money invested + the interest rate

money_amount, interest = input(
    "Please enter your investment amount and your interest rate: "
).split()

# convert the values to float data type and round the percentage to it to 2 decimal places
money_amount = float(money_amount)

interest = float(interest) * 0.01


# Cycle through 10 years using a for loop and range
for money in range(10):
    money_amount = money_amount + (money_amount * interest)

print("Your investment yield after 10 years is: {:.2f}".format(money_amount))
