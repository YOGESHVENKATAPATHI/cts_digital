import json

employees = {
    1: {"name": "Madhi", "salary": 50000},
    2: {"name": "John", "salary": 60000}
}

with open("emps.json", "w") as f:
    json.dump(employees, f)
