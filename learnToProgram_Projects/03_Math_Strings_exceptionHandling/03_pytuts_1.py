# Maths functions in python

# ---------- MATH MODULE ----------
# Python provides many functions with its Math module
import math

# Because you used import you access methods by referencing the module
print("ceil(4.4) = ", math.ceil(4.4))  # ceil rounds up a floating value to int
print("floor(4.4) = ", math.floor(4.4))  # floor rounds down a floating value to int
print("fabs(-4.4) = ", math.fabs(-4.4))  # fabs gives the absolute value of a number

# Factorial = 1 * 2 * 3 * 4
print("factorial(4) = ", math.factorial(4))

# Return remainder of division
print("fmod(5,4) = ", math.fmod(5, 4))

# Receive a float and return an int
print("trunc(4.2) = ", math.trunc(4.2))

# Return x^y
print("pow(2,2) = ", math.pow(2, 2))

# Return the square root
print("sqrt(4) = ", math.sqrt(4))

# Special values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

# Return e^x
print("exp(4) = ", math.factorial(4))

# Return the natural logarithm e * e * e ~= 20 so log(20) tells
# you that e^3 ~= 20
print("log(20) = ", math.log(20))

# You can define the base and 10^3 = 1000
print("log(1000,10) = ", math.log(1000, 10))

# You can also use base 10 like this
print("log10(1000) = ", math.log10(1000))

# We have the following trig and hyperbolic functions also available in python
# sin, cos, tan, asin, acos, atan, atan2, asinh, acosh,
# atanh, sinh, cosh, tanh

# Convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))
