# Create an empty dictionary to store the name and shoe size
shoe_sizes = {}

# Ask for the user's name and shoe size and store it in the dictionary
while True:
  name = input("Enter the name of the person: ")
  if name == "-1":
    break

  # Get the shoe size and store it in the dictionary
  shoe_size = int(input("Enter the shoe size: "))
  shoe_sizes[name] = shoe_size

# Ask the user for the name of the person they want to look up
while True:
  name = input("Enter the name of the person you want to look up: ")
  if name == "NA":
    break

  # Look up the shoe size and print it
  if name in shoe_sizes:
    print("The shoe size for", name, "is", shoe_sizes[name])
  else:
    print("Sorry, we don't have the shoe size for", name)
