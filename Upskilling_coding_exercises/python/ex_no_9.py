# Exercise 9

def greetings_user():
    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty")
        return

    print(f"Hello, {name}! Welcome.")


greetings_user()