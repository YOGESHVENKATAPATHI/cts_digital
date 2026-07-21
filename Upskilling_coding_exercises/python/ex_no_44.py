import csv

with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "salary"])
    writer.writerow(["Madhi", 60000])
