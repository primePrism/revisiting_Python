# First Task

# Have the user enter their investment amount and expectd interest
# Each year their investment will increase by their investment + their investment * interest rate
# Print out the earnings after a 10 year period


# Solution

# Ask for the money invested + the interest rate

moneyAmount = float(input("Enter your amount of money to invest: "))
interestValue = float(input("Enter the interest rate: "))

# convert the float point to 2 decimal places
interestValue = interestValue * 0.01


# Cycle through 10 years using a for loop and range
for year in range(1, 11):
    moneyAmount = moneyAmount + (moneyAmount * interestValue)

print("Your investment yield after 10 years is: {:.2f}".format(moneyAmount))
