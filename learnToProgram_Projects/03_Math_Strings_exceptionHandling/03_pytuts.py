# Exception handling is how we use certain strategies to handle error or prevent future error that can occur
# we use the try and except to handle error


while True:
    try:
        number = int(input("Enter a number: "))
        break

    except ValueError:
        # except valueError catches any error that is of different datatype as demanded.
        print("You did not enter a number")

    except:
        # just bring except will catch any type of error that will occur. not a very good idea :(
        print("Unknown Error occured")

print("Thanks for entering number {}".format(number))
