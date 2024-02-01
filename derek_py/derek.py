#!/usr/bin/python3

# Print a pine tree with a digit input.
print()
print("Hello! Let's print a pine tree together, shall we..\n")

# Get tree height and convert to integer.
tree_height = int(input("How tall is the tree.? "))

# starting spaces for the tree top, and the hashes..
spaces = tree_height - 1
hashes = 1

# save stump spaces for later
stump_spaces = tree_height - 1

# start the loop for the right number of rows.
while tree_height != 0:

    #print the spaces
    for i in range(spaces):
        print(" ", end="")

    #print the hashes to follow
    for i in range(hashes):
        print("#", end="")

    #print new line after each row
    print()


    #decrement spaces by 1
    spaces -= 1

    #increment hashes by 1
    hashes += 2

    #decrement tree hieght
    tree_height -= 1


for i in range(stump_spaces):
    print(" ", end="")

print("#")
