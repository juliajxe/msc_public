import sys


def menu():
    print("Menu:")
    print("1: Push")
    print("2: Pop")
    print("3: View")
    print("x: Exit")


stack = []

menu()

while True:
    opt = input()

    match opt:
        case "1":
            val = input("Enter the value to push: ")
            stack.append(val)
            print(f"Pushed {val}, enter a menu option")

        case "2":
            if len(stack) == 0:
                print("Can't pop - the stack is empty")
            else:
                val = stack.pop()
                print(f"Popped {val}, enter a menu option")

        case "3":
            print(stack)

        case "x":
            sys.exit()

        case "_":
            menu()
