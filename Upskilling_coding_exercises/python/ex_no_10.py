# Exercise 11

def kilograms_to_pounds():
    try:
        kg = float(input("Enter weight in kilograms: "))

        if kg <= 0:
            print("Weight must be positive")
            return

        lbs = kg * 2.20462

        print(f"Weight in Pounds: {lbs:.2f}")

    except ValueError:
        print("Invalid input")


kilograms_to_pounds()