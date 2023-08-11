# _______________Solve for X_____________
# x + 4 = 9


def solve_X(equation):
    x, add, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)

    return "x = " + str(num2 - num1)
