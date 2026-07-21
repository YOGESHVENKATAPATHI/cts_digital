# Exercise 19

def sum_odds():
    total = 0

    for i in range(10):
        if i % 2 == 0:
            continue

        total += i

    print(total)

sum_odds()
