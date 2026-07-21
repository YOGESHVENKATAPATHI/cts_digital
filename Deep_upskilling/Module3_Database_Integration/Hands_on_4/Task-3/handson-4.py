
""" Hands-On 4
Task 3 : N+1 Problem Demonstration
PostgreSQL + Python
"""

import psycopg2
import time

# PostgreSQL Connection

try:
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="college_database",
        user="postgres",
        password="YOUR_PASSWORD_HERE"
    )

    cursor = conn.cursor()

    print("=" * 60)
    print("Connected to PostgreSQL Successfully")
    print("=" * 60)

except Exception as e:
    print("Connection Failed")
    print(e)
    exit()


# STEP 56
# Simulate the N+1 Problem

print("\nSTEP 56 : N+1 Query Problem\n")

query_count = 0

start_time = time.time()

# First Query
cursor.execute("""
SELECT *
FROM enrollments;
""")

query_count += 1

enrollments = cursor.fetchall()

print("Enrollment Records :", len(enrollments))
print()

for enrollment in enrollments:

    student_id = enrollment[1]

    cursor.execute(
        """
        SELECT first_name,last_name
        FROM students
        WHERE student_id=%s;
        """,
        (student_id,)
    )

    student = cursor.fetchone()

    query_count += 1

    print(
        student[0],
        student[1],
        "-> Enrollment ID:",
        enrollment[0]
    )

end_time = time.time()

print("\nN+1 VERSION")
print("--------------------------")
print("Queries Executed :", query_count)
print("Execution Time   :", round(end_time - start_time, 6), "seconds")


# STEP 57
# Optimized JOIN Query

print("\nSTEP 57 : Optimized JOIN Query\n")

start_time = time.time()

cursor.execute("""
SELECT
    e.enrollment_id,
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id;
""")

rows = cursor.fetchall()

end_time = time.time()

print("JOIN VERSION")
print("--------------------------")

for row in rows:

    print(
        row[1],
        row[2],
        "->",
        row[3]
    )

print("\nQueries Executed : 1")
print("Execution Time   :", round(end_time - start_time, 6), "seconds")


# STEP 58 Comparison

print("\nSTEP 58 : Comparison\n")

print("N+1 Version")
print("Queries :", query_count)

print()

print("JOIN Version")
print("Queries : 1")

print()

print("Reduction in Queries :", query_count - 1)

# STEP 59 Documentation

print("\nSTEP 59 : Observation\n")

print("""
Observation
-----------

1. N+1 Version

   One query retrieves all enrollments.

   One additional query is executed
   for every enrollment to retrieve
   student details.

   Total Queries = 1 + N

2. Optimized Version

   A single JOIN query retrieves

   • Enrollment
   • Student
   • Course

   together.

   Total Queries = 1

3. For a database with 10,000 enrollments

   N+1 Version

   = 10001 SQL Queries

   Optimized JOIN Version

   = 1 SQL Query

Conclusion

Using JOIN reduces database round trips,
improves performance and avoids the
N+1 Query Problem.
""")

# Close Connection

cursor.close()
conn.close()

print("Database Connection Closed")
