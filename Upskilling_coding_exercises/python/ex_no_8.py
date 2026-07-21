# Exercise 8

def salary_stats(salaries):
    if not salaries:
        return "Salary list empty"

    highest = max(salaries)
    lowest = min(salaries)

    return f"Highest Salary: ₹{highest}\nLowest Salary: ₹{lowest}"


salary_list = [50000, 75000, 62000, 95000]

print(salary_stats(salary_list))