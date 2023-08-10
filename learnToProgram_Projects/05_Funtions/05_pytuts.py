# Everything Functions
# turnig the previous code into a function
import random


def ceasorCypher(message):
    encryptKey = random.randint(1, 27)

    secretMessage = ""

    for char in message:
        if char.isalpha():
            charCode = ord(char)
            charCode += encryptKey

            if char.isupper():
                if charCode > ord("Z"):
                    charCode -= 26

                if charCode < ord("A"):
                    charCode += 26

            else:
                if charCode > ord("z"):
                    charCode -= 26

                if charCode < ord("a"):
                    charCode += 26

            secretMessage += chr(charCode)

        else:
            secretMessage += char

    print("Encrypted message: ", secretMessage)


askuser = input("Enter a message: ")
ceasorCypher(askuser)
