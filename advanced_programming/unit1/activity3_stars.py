import sys


def input_menu():
    option = None

    while option not in {"d", "l", "r", "x"}:
        print("Enter your choice of shape:")
        print("d: Diamond")
        print("l: Left-aligned triangle")
        print("r: Right-aligned triangle")
        print("x: Exit")

        option = input()

    if option == "x":
        sys.exit()

    return option


shape = input_menu()

symbol = input("Enter the symbol to use: ")
width = int(input("Enter the width of the shape: "))

if shape == "d" and width % 2 == 0:
    raise ValueError("A diamond must have an odd width")

if shape in {"l", "r"}:
    for i in range(width):
        line = symbol * (i+1)

        if shape == "r":
            line = line.rjust(width)

        print(line)

if shape == "d":
    for i in range(0, width, 2):
        line = symbol * (i+1)
        print(line.center(width))

    for i in range(width-2, 0, -2):
        line = symbol * i
        print(line.center(width))
