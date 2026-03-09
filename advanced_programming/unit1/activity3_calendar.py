def print_line(vals):
    line = ""

    for i in range(7):
        line += vals[i].rjust(4)

    print(line)


HEADER = ["M", "T", "W", "Th", "F", "S", "Su"]

days = int(input("Number of days in month: "))

if days < 28 or days > 31:
    raise ValueError("A month may only have 28, 29, 30 or 31 days")

first = int(input("First day of month (1 = Monday, 7 = Sunday): "))

if first < 1 or first > 7:
    raise ValueError("Invalid first day of month")

cal = ["" for _ in range(first-1)] + \
      [str(j) for j in range(1, days+1)] + \
      ["" for _ in range(days+1, 42)]

print_line(HEADER)

for k in range(0, 42, 7):
    print_line(cal[k:k+7])
