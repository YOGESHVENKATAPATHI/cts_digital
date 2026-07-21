# Exercise 5

def display_coordinate(co_ords):
    if len(co_ords) != 2:
        return "Invalid Coordinates"

    x, y = co_ords
    return f"X = {x}, Y = {y}"


coordinates = (15, 25)

print(display_coordinate(coordinates))