# Exercise 4

def calculate_net_salary(sal, tax_rate):
    if sal <= 0:
        return "Invalid Salary"

    if not (0 <= tax_rate <= 1):
        return "Invalid Tax Rate"

    net_salary = sal - (sal * tax_rate)
    return f"Net Salary: ₹{net_salary:.2f}"


sal = 75000.5
tax_rate = 0.18

print(calculate_net_salary(sal, tax_rate))