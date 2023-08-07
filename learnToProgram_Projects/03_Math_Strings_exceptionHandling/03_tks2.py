# Converting strings into its unicode charaters

# Receive a uppercase string and then hide its meaning by turning
# it into a string of unicodes
# Then translate it from unicode back into its original meaning


# accept user's normal string
normalString = input("Enter sentence to be hidden: ")

# an empty variable to hold character is input string
secretEncoding = ""

# cycle through each character in sentence
for letter in normalString:
    # store each letter in a new string
    secretEncoding += str(ord(letter) - 23)

print("secret Message is: ", secretEncoding)


# converting secret message back to normal message

normalString = ""
for i in range(0, len(secretEncoding) - 1, 2):
    # get the 1st and 2nd of the 2 digit number
    letterCode = secretEncoding[i] + secretEncoding[i + 1]

    # convert the code into characters and add them to a new string
    normalString += chr(int(letterCode) + 23)

print("Original Message: ", normalString)
