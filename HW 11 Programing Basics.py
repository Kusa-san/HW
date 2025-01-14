counter = 1
lines = 5
stars = 1
spaces = lines

increse = True

while counter > 0:

    print("  " * spaces, end="")

    print("* " * stars)

    if increse:

        counter += 1
        spaces -= 1
        stars += 2

        if counter > lines:

            increse = False
            counter -= 2
            spaces += 2
            stars -= 4
    else:

        counter -= 1
        spaces += 1
        stars -= 2