# This task is about printing a tree fig based on a user input

""" 
To do

- Decreament spaces by 1 each time through the loop
- Increament the hashes by 2 each time through the loop
- Save spaces to the stump by calculating tree height -1
- Decrease from tree height until it equals 0
- print spaces and then hashes for each row
- peint stump spaces and then 1 hash
"""

# get the number of rows for the tree height
# # Convert into an integer
tree_height = int(input("Enter a number for the tree height: "))


# Get the starting spaces for the top of the tree
spaces = tree_height - 1

# There is one hashtag to start that will be increamented
hashes = 1

# Save stump spaces till later
stump_spaces = tree_height - 1

# Make sure the right number of rows are printed
while tree_height != 0:

# print the spaces using end='' in print
    for i in range(spaces):
        print(' ', end="")

# Print the hashes
    for i in range(hashes):
        print('#', end="")

# Newline after each row is printed
    print()
# That is decreamented by 1 each time
    spaces -= 1 

# that hashes is increamented by 2 each time
    hashes += 2

# Decrement tree height each time to jump out of the loop
    tree_height -= 1

# Print the spaces before the stump and then the hash
for i in range(stump_spaces):
    print(' ', end="")

print("#")
