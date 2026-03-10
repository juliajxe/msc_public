import Conversion


def get_function():
    print("Conversion menu:")
    print("1: Feet and inches to meters")
    print("2: Pounds to kilograms")
    print("3: Kelvin to celsius")
    print("4: Hours and minutes to seconds")
    print("x: Exit")

    return input()


opt = None

while opt != "x":
    opt = get_function()

    try:
        match opt:
            case "1":
                feet = float(input("Feet: "))
                inches = float(input("Inches: "))
                result = Conversion.to_meters(feet, inches)
                print(f"Meters = {result}")
            case "2":
                pounds = float(input("Pounds: "))
                result = Conversion.to_kilograms(pounds)
                print(f"Kilograms = {result}")
            case "3":
                kelvin = float(input("Kelvin: "))
                result = Conversion.to_celsius(kelvin)
                print(f"Celsius = {result}")
            case "4":
                hours = float(input("Hours: "))
                minutes = float(input("Minutes: "))
                result = Conversion.to_seconds(hours, minutes)
                print(f"Seconds = {result}")
    except Exception as e:
        print("Could not convert due to an error:")
        print(repr(e))
