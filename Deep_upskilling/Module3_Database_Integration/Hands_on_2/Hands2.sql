-- Task 1: Insert, Update and Delete Data.

-- Data for Departments Table
INSERT INTO departments (dept_name, head_of_dept, budget)
VALUES
('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
('Electronics', 'Dr. Priya Nair', 620000.00),
('Mechanical', 'Dr. Suresh Iyer', 540000.00),
('Civil', 'Dr. Ananya Sharma', 430000.00);

SELECT * FROM departments;

-- Data for Students Table
INSERT INTO students (first_name,last_name,email,date_of_birth,department_id,enrollment_year)
VALUES
('Arjun','Mehta','arjun.mehta@college.edu','2003-04-12',1,2022),
('Priya','Suresh','priya.suresh@college.edu','2003-07-25',1,2022),
('Rohan','Verma','rohan.verma@college.edu','2002-11-08',2,2021),
('Sneha','Patel','sneha.patel@college.edu','2004-01-30',3,2023),
('Vikram','Das','vikram.das@college.edu','2003-09-14',1,2022),
('Kavya','Menon','kavya.menon@college.edu','2002-05-17',2,2021),
('Aditya','Singh','aditya.singh@college.edu','2004-03-22',4,2023),
('Deepika','Rao','deepika.rao@college.edu','2003-08-09',1,2022);

SELECT COUNT(*) FROM students;

-- Data for Courses Table
INSERT INTO courses (course_name,course_code,credits,department_id)
VALUES
('Data Structures & Algorithms','CS101',4,1),
('Database Management Systems','CS102',3,1),
('Object Oriented Programming','CS103',4,1),
('Circuit Theory','EC101',3,2),
('Thermodynamics','ME101',3,3);

SELECT COUNT(*) FROM courses;

-- Data for Enrollments Table
INSERT INTO enrollments (student_id,course_id,enrollment_date,grade)
VALUES
(1,1,'2022-07-01','A'),
(1,2,'2022-07-01','B'),
(2,1,'2022-07-01','B'),
(2,3,'2022-07-01','A'),
(3,4,'2021-07-01','A'),
(4,5,'2023-07-01',NULL),
(5,1,'2022-07-01','C'),
(5,2,'2022-07-01','A'),
(6,4,'2021-07-01','B'),
(7,5,'2023-07-01',NULL),
(8,1,'2022-07-01','A'),
(8,3,'2022-07-01','B');

SELECT COUNT(*) FROM enrollments;

-- Data for Professors Table
INSERT INTO professors (prof_name,email,department_id,salary)
VALUES
('Dr. Anand Krishnan','anand.k@college.edu',1,95000.00),
('Dr. Meena Pillai','meena.p@college.edu',1,88000.00),
('Dr. Sunil Rajan','sunil.r@college.edu',2,82000.00),
('Dr. Latha Gopal','latha.g@college.edu',3,79000.00),
('Dr. Kartik Bose','kartik.b@college.edu',4,76000.00);

SELECT COUNT(*) FROM professors;

-- Data for Students Table (Additional Entries)
INSERT INTO students(first_name,last_name,email,date_of_birth,department_id,enrollment_year)
VALUES
('Annapoorani','Alagananthan','annapoorani@college.edu','2004-06-15',1,2023),
('Rahul','Kumar','rahul.kumar@college.edu','2003-12-20',2,2022);

SELECT * FROM students;
SELECT COUNT(*) FROM students;

-- Update

-- Update Vikram's grade from C → B.
UPDATE enrollments SET grade = 'B' WHERE student_id = 5 AND course_id = 1;
SELECT * FROM enrollments WHERE student_id = 5 AND course_id = 1;

-- Delete

-- Delete all enrollments with NULL grades.
SELECT * FROM enrollments WHERE grade IS NULL;
DELETE FROM enrollments WHERE grade IS NULL;

-- Verify Counts after Deletion 
SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM enrollments;

-- Task 2: Single Table Queries

-- Get Students enrolled in 2022
SELECT * FROM students WHERE enrollment_year = 2022 ORDER BY last_name;

-- Get Courses with more than 3 credits
SELECT * FROM courses WHERE credits > 3 ORDER BY credits DESC;

-- Get Professors with salary between 80000 and 95000
SELECT * FROM professors WHERE salary BETWEEN 80000 AND 95000;

-- Get Students with emails ending with @college.edu
SELECT * FROM students WHERE email LIKE '%@college.edu';

-- Count students per enrollment year
SELECT enrollment_year, COUNT(*) AS total_students FROM students GROUP BY enrollment_year ORDER BY enrollment_year;

-- Task 3: Multi-Table Queries

-- Get Student name + Department
SELECT s.first_name || ' ' || s.last_name AS student_name,d.dept_name FROM students s JOIN departments d ON s.department_id = d.department_id;

-- Get Enrollment + Student + Course
SELECT s.first_name,s.last_name,c.course_name,e.grade FROM enrollments e JOIN students s ON e.student_id = s.student_id JOIN courses c ON e.course_id = c.course_id;

-- Get Students not enrolled in any course
SELECT s.student_id,s.first_name,s.last_name FROM students s LEFT JOIN enrollments e ON s.student_id = e.student_id WHERE e.student_id IS NULL;

-- Get Course wise enrollment count
SELECT c.course_name, COUNT(e.student_id) AS enrollment_count FROM courses c LEFT JOIN enrollments e ON c.course_id = e.course_id GROUP BY c.course_id,c.course_name ORDER BY c.course_name;

-- Get Departments with professors
SELECT d.dept_name,p.prof_name,p.salary FROM departments d LEFT JOIN professors p ON d.department_id = p.department_id;

-- Task 4: Aggregations

-- Get Enrollment count per course
SELECT c.course_name,COUNT(e.enrollment_id) AS enrollment_count FROM courses c LEFT JOIN enrollments e ON c.course_id = e.course_id GROUP BY c.course_name;

-- Get Average salary by department
SELECT d.dept_name,ROUND(AVG(p.salary),2) AS avg_salary FROM departments d LEFT JOIN professors p ON d.department_id = p.department_id GROUP BY d.dept_name;

-- Get Departments with budget > 600000
SELECT * FROM departments WHERE budget > 600000;

-- Get Grade distribution for CS101
SELECT e.grade,COUNT(*) AS total FROM enrollments e JOIN courses c ON e.course_id = c.course_id WHERE c.course_code = 'CS101' GROUP BY e.grade;

-- Get Departments with more than 2 enrolled students
SELECT d.dept_name,COUNT(e.student_id) AS total_students FROM departments d JOIN courses c ON d.department_id = c.department_id JOIN enrollments e ON c.course_id = e.course_id GROUP BY d.dept_name HAVING COUNT(e.student_id) > 2;