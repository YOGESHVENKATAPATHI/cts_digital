# Exercise 18

def first_even(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)
            break

first_even(11, 20)
