from datetime import datetime

tasks = [
    ("Project", datetime(2026, 1, 15)),
    ("Assignment", datetime(2025, 12, 1))
]

tasks.sort(key=lambda x: x[1])
print(tasks)
