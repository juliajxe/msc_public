import sys
from collections import deque


def menu():
    print("Menu:")

    print("1: " + str_add.capitalize())
    print("2: " + str_del.capitalize())
    print("3: View")
    print("x: Exit")


def add_val():
    val = input(f"Enter the value to {str_add}: ")
    ds.append(val)
    print(f"Added {val}, enter a menu option")


def del_val():
    if len(ds) == 0:
        print("The data structure is empty")
        return

    if ds_type == "q":
        val = ds.popleft()
    else:
        val = ds.pop()
    print(f"Removed {val}, enter a menu option")


ds_type = input("Select data structure, enter q for queue or s for stack: ")

if ds_type not in {"q", "s"}:
    raise ValueError("Invalid option")

if ds_type == "q":
    ds = deque()

    str_add = "enqueue"
    str_del = "dequeue"
else:
    ds = []

    str_add = "push"
    str_del = "pop"

menu()

while True:
    opt = input()

    match opt:
        case "1":
            add_val()

        case "2":
            del_val()

        case "3":
            print([val for val in ds])

        case "x":
            sys.exit()

        case "_":
            menu()
