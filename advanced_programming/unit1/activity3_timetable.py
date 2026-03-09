mult = int(input("Enter an integer: "))

print("The even timetable for {mult} is:")

for i in range(2, 22, 2):
    print(f"{i:2} times {mult} is {i * mult}")
