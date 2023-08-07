# A simple number guessing game with do_while loops

import random

hiddenNumber = random.randrange(1, 6)

while True:
    try:
        guessNum = int(input("Enter a number between 0 and 6: "))
        if (guessNum >= 1) and (guessNum <= 5):  # To check for the range
            if guessNum == hiddenNumber:
                print("Congratulations, you are great at guessing.")
                break  # Break out of the loop when the guess is correct

            else:
                print("Sorry, try your luck again.")

        else:
            print("Number is out of range.")
            continue  # Continue to the next iteration of the loop

    except ValueError:
        print("Invalid Input. Enter a valid number.")

    except:
        print("Unknown Error Occurred.")

print("Game Over.")
