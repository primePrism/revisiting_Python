# _______________Solve for X_____________
# x + 4 = 9


def solve_X(equation):
    x, add, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)

    return "x = " + str(num2 - num1)


def isPrime(num):
    for x in range(2, num):
        if (num % x) == 0:
            return False

    return True


def getPrimes(maxNumber):
    list_of_primes = []

    for num1 in range(2, maxNumber):
        if isPrime(num1):
            list_of_primes.append(num1)

    return list_of_primes


max_num_to_check = int(input("Search for primes up to: "))

list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:
    print(prime)
