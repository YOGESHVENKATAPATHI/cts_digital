-- Advanced SQL – PostgreSQL

-- TASK 1 : SUBQUERIES


-- QN 35. Students enrolled in more courses than the average

SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) avg_table
);


-- QN 36. Courses where every enrolled student received grade A

SELECT
    c.course_name,
    c.course_code
FROM courses c
WHERE NOT EXISTS
(
    SELECT 1
    FROM enrollments e
    WHERE e.course_id = c.course_id
      AND e.grade <> 'A'
);


-- QN 37. Highest paid professor in each department

SELECT
    p.prof_name,
    d.dept_name,
    p.salary
FROM professors p
JOIN departments d
ON p.department_id = d.department_id
WHERE p.salary =
(
    SELECT MAX(salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);


-- QN 38. Departments whose average professor salary > 85000

SELECT * FROM
(
    SELECT
        d.department_id,
        d.dept_name,
        AVG(p.salary) AS avg_salary
    FROM departments d
    JOIN professors p
    ON d.department_id = p.department_id
    GROUP BY d.department_id,d.dept_name
) dept_avg
WHERE avg_salary > 85000;


-- TASK 2 : VIEWS


-- QN 39. Student Enrollment Summary View

CREATE OR REPLACE VIEW vw_student_enrollment_summary AS
SELECT s.student_id, s.first_name || ' ' || s.last_name AS student_name, d.dept_name,
COUNT(e.course_id) AS total_courses,ROUND( AVG(
CASE WHEN grade='A' THEN 4
WHEN grade='B' THEN 3
WHEN grade='C' THEN 2
WHEN grade='D' THEN 1
WHEN grade='F' THEN 0
END),2) AS gpa
FROM students s
LEFT JOIN departments d
ON s.department_id=d.department_id
LEFT JOIN enrollments e
ON s.student_id=e.student_id
GROUP BYs.student_id, student_name, d.dept_name;

-- Test View
SELECT * FROM vw_student_enrollment_summary;


-- QN 40. Course Statistics View

CREATE OR REPLACE VIEW vw_course_stats AS
SELECT c.course_name, c.course_code, COUNT(e.student_id) AS total_enrollments,
ROUND(AVG(CASE
WHEN grade='A' THEN 4
WHEN grade='B' THEN 3
WHEN grade='C' THEN 2
WHEN grade='D' THEN 1
WHEN grade='F' THEN 0
END),2) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY c.course_name,c.course_code;

-- Test View
SELECT * FROM vw_course_stats


-- QN 41. Students having GPA > 3

SELECT * FROM vw_student_enrollment_summary WHERE gpa > 3;


-- QN 42. Attempt Update

UPDATE vw_student_enrollment_summary SET student_name='Demo' WHERE student_id=1;

-- PostgreSQL throws an error because complex views involving multiple tables, GROUP BY and 
-- aggregate functions are not automatically updatable.


-- QN 43. Drop Views

DROP VIEW IF EXISTS vw_course_stats;

DROP VIEW IF EXISTS vw_student_enrollment_summary;


-- Recreating the Single Table View with CHECK OPTION

CREATE VIEW vw_students_cs AS
SELECT * FROM students WHERE department_id=1 WITH LOCAL CHECK OPTION;


-- Task 3: Stored Procedures and Transactions

-- Function to Enroll Student

CREATE OR REPLACE FUNCTION fn_enroll_student(p_student INT,p_course INT,p_date DATE)
RETURNS TEXT
LANGUAGE plpgsql
AS
$$
BEGIN
IF EXISTS (SELECT 1 FROM enrollments WHERE student_id=p_student AND course_id=p_course)
THEN
RETURN 'Duplicate Enrollment';
END IF;
INSERT INTO enrollments(student_id,course_id,enrollment_date) VALUES(p_student,p_course,p_date);
RETURN 'Enrollment Successful';
END;
$$;

-- Test Function

SELECT fn_enroll_student(2,2,CURRENT_DATE);

-- QN 45: Transfer Log Table

CREATE TABLE IF NOT EXISTS department_transfer_log
(
log_id SERIAL PRIMARY KEY,
student_id INT,
old_department INT,
new_department INT,
transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Transfer Function

CREATE OR REPLACE FUNCTION fn_transfer_student(p_student INT,new_department INT)
RETURNS VOID
LANGUAGE plpgsql
AS
$$
DECLARE old_department INT;
BEGIN
SELECT department_id INTO old_department FROM students WHERE student_id=p_student;
UPDATE students SET department_id=new_department WHERE student_id=p_student;
INSERT INTO department_transfer_log(student_id,old_department,new_department) VALUES(p_student,old_department,new_department);
END;
$$;

-- Execute

SELECT fn_transfer_student(1,2);

-- Verify

SELECT * FROM department_transfer_log;
SELECT student_id, department_id FROM students WHERE student_id = 1;

-- QN 46: Transaction & Rollback

BEGIN;
UPDATE students SET department_id = 3 WHERE student_id = 2;
INSERT INTO department_transfer_log(student_id,old_department,new_department) VALUES(9999,1,3);
ROLLBACK;

-- Verify rollback

SELECT student_id, department_id FROM students WHERE student_id = 2;

-- Savepoint

BEGIN;
INSERT INTO enrollments(student_id, course_id, enrollment_date) VALUES(12,1,CURRENT_DATE);
SAVEPOINT first_insert;

-- Intentionally fail:

INSERT INTO invalid_table VALUES (1);

-- recover to savepoint

ROLLBACK TO SAVEPOINT first_insert;

-- Commit the transaction

COMMIT;

-- Verify
SELECT * FROM enrollments WHERE student_id = 10 AND course_id = 1;