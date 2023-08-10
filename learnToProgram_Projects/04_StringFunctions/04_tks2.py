# Ceasar Cypher Encryption

# A - Z 65 - 90
# a -z 97 - 122
# ord(your letter) change your letter to unicode
# chr(your code) change your unicode to letter


# Receive the message to encrypt and the number of characters to shift
message = input("Enter your message to be encrypted: ")
encryptKey = int(input("Enter a number between 0 - 27 to serve as an encryption key: "))

# Prepare your secret message
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

# To decrypt the only thing that changes is the sign of the key
DecryptedMessage = ""
encryptKey = -encryptKey


for char in secretMessage:
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
        DecryptedMessage += chr(charCode)

    # If not a letter leave the character as is
    else:
        DecryptedMessage += char

print("Decrypted message: ", DecryptedMessage)
