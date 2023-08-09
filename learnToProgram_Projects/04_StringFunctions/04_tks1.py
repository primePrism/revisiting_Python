# _______________ Acronym Generator_________________

input_String = input("Please enter your phrase: ")

input_String = input_String.upper()

listWords = input_String.split()

for words in listWords:
    print(words[0], end="")

print()
