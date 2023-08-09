# Ceasar Cypher Encryption

# A - Z 65 - 90
# a -z 97 - 122
# ord(your letter) change your letter to unicode
# chr(your code) change your unicode to letter


# Receive the message to encrypt and the number of characters to shift

# Prepare your secret message

# Cycle through each character in the message

    # If it isn't a letter then keep it as it is in the else below

        # Get the character code and add the shift amount

        # If uppercase then compare to uppercase unicodes

            # If bigger than Z subtract 26
            
            # If smaller than A add 26
            
        # Do the same for lowercase characters

        # Convert from code to letter and add to message

    # If not a letter leave the character as is


# To decrypt the only thing that changes is the sign of the key