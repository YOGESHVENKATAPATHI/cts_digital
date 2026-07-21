def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")

divide(20, 5)