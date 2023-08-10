# Everything Functions
# turnig the previous code into a function
import random


def ceasorCypher(message):
    encryptKey = random.randint(1, 27)

    secretMessage = ""

    # Cycle through each character in the message
    for char in message:
        # If it isn't a letter then keep it as it is in the else below
        if char.isalpha():
            # Get the character code and add the shift amount
            charCode = ord(char)
            charCode += encryptKey

            # If uppercase then compare to uppercase unicodes
            if char.isupper():
                # If bigger than Z subtract 26
                if charCode > ord("Z"):
                    charCode -= 26

                # If smaller than A add 26
                if charCode < ord("A"):
                    charCode += 26
            # Do the same for lowercase characters
            else:
                if charCode > ord("z"):
                    charCode -= 26

                if charCode < ord("a"):
                    charCode += 26

            # Convert from code to letter and add to message
            secretMessage += chr(charCode)

        # If not a letter leave the character as is
        else:
            secretMessage += char

    print("Encrypted message: ", secretMessage)


askuser = input("Enter a message: ")
ceasorCypher(askuser)
