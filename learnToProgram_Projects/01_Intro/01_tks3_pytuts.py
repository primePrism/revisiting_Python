# If age is 5, Go to Kindergarten
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater than 17, then output go to college
# try to complete this in less than 10 lines of code

# ***My SOLUTION***

age = eval(input("Enter your age: "))
# eval automatically convert user inputs to type ints

if age == 5:
    print("Go to Kindergarten")

elif (age >= 6) and (age <= 17):
    print("You qaulify for grade 1 to 12")

elif age > 17:
    print("Go to college")
