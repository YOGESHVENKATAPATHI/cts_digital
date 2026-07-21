# Exercise 15

def validate_user(user, pwd):
    if user == "admin":
        if pwd == "pass123":
            print("Login Successful")
        else:
            print("Incorrect Password")
    else:
        print("Invalid User")

validate_user("admin", "pass123")
