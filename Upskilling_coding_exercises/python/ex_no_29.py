def read_file():
    try:
        with open("greeting.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")

read_file()