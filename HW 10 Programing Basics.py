counter = 1
lines = 5
stars = 1
spaces = lines

while counter <= lines:

    print("  " * spaces, end="")

    print("* " * stars)

    counter += 1
    spaces -= 1
    stars += 2