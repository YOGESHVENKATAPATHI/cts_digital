staff_roster = []

staff_roster.append(["S201", "Priya", "Software Engineer"])
staff_roster.append(["S202", "Rahul", "QA Analyst"])
staff_roster.append(["S203", "Kavya", "UX Researcher"])

print("--- Current Staff Roster ---")
for staff in staff_roster:
    print(staff)

target_staff_id = "S202"
print(f"\\nSearching for Staff ID: {target_staff_id}")

for staff in staff_roster:
    if staff[0] == target_staff_id:
        print("-> Staff Member Located:")
        print(staff)
        break

# Removing the first entry
staff_roster.pop(0)

print("\\n--- Roster After Departure ---")
for staff in staff_roster:
    print(staff)