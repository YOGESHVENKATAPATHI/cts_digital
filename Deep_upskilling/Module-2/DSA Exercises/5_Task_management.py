project_tasks = []

project_tasks.append(["T001", "Database Migration", "High"])
project_tasks.append(["T002", "UI Redesign", "Medium"])
project_tasks.append(["T003", "API Documentation", "Low"])

print("--- Initial Task List ---")
for task in project_tasks:
    print(task)

target_task_id = "T003"
print(f"\\nSearching for Task ID: {target_task_id}")

for task in project_tasks:
    if task[0] == target_task_id:
        print("-> Task Found:")
        print(task)
        break

# Simulating task completion
completed_task = project_tasks.pop(1)
print(f"\\nCompleted and Removed Task: {completed_task[1]}")

print("\\n--- Remaining Tasks ---")
for task in project_tasks:
    print(task)