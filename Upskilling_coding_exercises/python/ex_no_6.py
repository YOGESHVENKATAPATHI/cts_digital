# Exercise 6

def check_even_odd(number):
    if not isinstance(number, int):
        return "Invalid Input"

    return "Even" if number % 2 == 0 else "Odd"


number = 17

print(check_even_odd(number))