-- Task 1: Create the Database and Tables

-- Departments

CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY, dept_name VARCHAR(100) NOT NULL, hod_name VARCHAR(100), budget DECIMAL(12,2));

-- Students

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL, date_of_birth DATE, department_id INT, enrollment_year INT,
    CONSTRAINT fk_student_department
    FOREIGN KEY(department_id)
    REFERENCES departments(department_id)
);

-- Courses

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,

    CONSTRAINT fk_course_department
    FOREIGN KEY(department_id)
    REFERENCES departments(department_id)
);

-- Enrollments

CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY, student_id INT, course_id INT, enrollment_date DATE, grade CHAR(2),
    CONSTRAINT fk_enrollment_student
    FOREIGN KEY(student_id)
    REFERENCES students(student_id),
    CONSTRAINT fk_enrollment_course
    FOREIGN KEY(course_id)
    REFERENCES courses(course_id)
);

-- Professors

CREATE TABLE professors (
    professor_id SERIAL PRIMARY KEY, prof_name VARCHAR(100) NOT NULL, email VARCHAR(100) UNIQUE, 
	department_id INT, salary DECIMAL(10,2),
    CONSTRAINT fk_professor_department
    FOREIGN KEY(department_id)
    REFERENCES departments(department_id)
);

-- Show the created tables

SELECT table_name FROM information_schema.tables WHERE table_schema='public';


-- Task 3: Alter and Extend the Schema

-- Alterations to the existing tables to add new columns, constraints, and rename columns.

ALTER TABLE students ADD COLUMN phone_number VARCHAR(15);
ALTER TABLE courses ADD COLUMN max_seats INT DEFAULT 60;
ALTER TABLE enrollments ADD CONSTRAINT chk_grade CHECK (grade IN ('A','B','C','D','F') OR grade IS NULL);
ALTER TABLE departments RENAME COLUMN hod_name TO head_of_dept;
ALTER TABLE students DROP COLUMN phone_number;

-- Verification of table alterations

-- Verify departments table

SELECT column_name FROM information_schema.columns WHERE table_name='departments';

-- Verify courses table

SELECT column_name FROM information_schema.columns WHERE table_name='courses';

-- Verify students table

SELECT column_name FROM information_schema.columns WHERE table_name='students';

-- Verify CHECK Constraint

SELECT conname FROM pg_constraint WHERE conname = 'chk_grade';