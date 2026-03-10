import sys
from collections import deque


def menu():
    print("Menu:")
    print("1: Enqueue")
    print("2: Dequeue")
    print("3: View")
    print("x: Exit")


q = deque()

menu()

while True:
    opt = input()

    match opt:
        case "1":
            val = input("Enter the value to enqueue: ")
            q.append(val)
            print(f"Enqueued {val}, enter a menu option")

        case "2":
            if len(q) == 0:
                print("Can't dequeue - the queue is empty")
            else:
                val = q.popleft()
                print(f"Dequeued {val}, enter a menu option")

        case "3":
            print([val for val in q])

        case "x":
            sys.exit()

        case "_":
            menu()
