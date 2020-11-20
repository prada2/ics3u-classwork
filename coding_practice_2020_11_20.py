# Create a program that will ask the user for their favourite colour. Have the program output a message saying something like: "Blue?! No way, that's my favourite colour too!".
name = input("What is your name? ")
print("Hello " + name)
colour = input("What is your favourite colour? ")
print(f"{colour}! No way, that's my favourite colour too!")


# Create a program that asks how many cans come in a pack. Then ask the user how many packs there are. Output a message indicating the total number of cans.
cans = input("How many cans come in the pack? ")
packs = input("How many packs are there? ")
total_number_of_cans = int(cans) * int(packs) 
print("Total cans: ", total_number_of_cans)


# Ask the user for the three dimensions of a rectangular prism. Output the volume.
length = input("What the length? ")
width = input("What is the width? ")
height = input("What is the height? ")
volume = int(length) * int(width) * int(height)
print("Volume of rectangular prism: ", volume)
