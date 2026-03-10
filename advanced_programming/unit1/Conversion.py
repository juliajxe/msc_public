def to_meters(feet, inches):
    if feet < 0:
        raise ValueError("Feet must be positive")
    if inches < 0:
        raise ValueError("Inches must be positive")
    if inches >= 12:
        raise ValueError("Inches must be less than 12")

    return (feet + inches/12) * 0.3048


def to_kilograms(pounds):
    if pounds < 0:
        raise ValueError("Pounds must be positive")

    return pounds * 0.453592


def to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin must be positive")

    return kelvin - 273.15


def to_seconds(hours, minutes):
    if hours < 0:
        raise ValueError("Hours must be positive")
    if minutes < 0:
        raise ValueError("Minutes must be positive")
    if minutes >= 60:
        raise ValueError("Minutes must be less than 60")

    return (hours*60 + minutes) * 60
