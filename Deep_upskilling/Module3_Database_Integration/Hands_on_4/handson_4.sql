-- Hands-On 4
-- Query Optimization – Indexes, EXPLAIN & the N+1 Problem

-- TASK 1 : BASELINE PERFORMANCE (NO INDEXES)


-- QN 48: EXPLAIN on the JOIN query
EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;


-- QN 49: Observation

-- The EXPLAIN output shows Sequential Scan (Seq Scan)
-- on both the enrollments and students tables.
--
-- PostgreSQL chooses Seq Scan because the tables contain
-- only a small number of rows, making a full table scan
-- more efficient than using an index.

-- QN 50: Estimated Cost

-- Estimated Cost from EXPLAIN:

-- Overall Query Cost
-- Startup Cost : 12.16
-- Total Cost   : 42.16

-- Students Table
-- Startup Cost : 0.00
-- Total Cost   : 12.00

-- Enrollments Table
-- Startup Cost : 0.00
-- Total Cost   : 24.50

-- PostgreSQL estimates the execution cost before
-- running the query. Lower cost generally indicates
-- a more efficient execution plan.

-- TASK 2 : CREATE INDEXES

-- QN 51: B-Tree Index
CREATE INDEX idx_students_enrollment_year ON students(enrollment_year);

-- Verify
SELECT * FROM pg_indexes WHERE tablename='students';


-- QN 52: Composite UNIQUE Index

CREATE UNIQUE INDEX idx_enrollment_unique ON enrollments(student_id,course_id);

-- Verify
SELECT * FROM pg_indexes WHERE tablename='enrollments';


-- QN 53: Index on Course Code
CREATE INDEX idx_course_code ON courses(course_code);

-- Verify
SELECT * FROM pg_indexes WHERE tablename='courses';


-- QN 54: Compare Query Plan

EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id=e.student_id
JOIN courses c
ON c.course_id=e.course_id
WHERE s.enrollment_year=2022;


-- Step 54: Compare Query Plans

-- Before Creating Indexes
-- Overall Cost : 12.16..42.16
-- Seq Scan was used on students and enrollments.
-- Courses table used the primary key index.

-- After Creating Indexes
-- Overall Cost : 1.14..3.41
-- Seq Scan is still used because the tables contain
-- only a small number of rows.
-- However, the estimated execution cost has reduced
-- significantly, indicating that the query plan is
-- more efficient.

-- PostgreSQL automatically chooses the most efficient
-- execution strategy based on table size and statistics.

-- QN 55: Partial Index

CREATE INDEX idx_null_grades
ON enrollments(student_id)
WHERE grade IS NULL;

-- Verify Partial Index

SELECT indexname
FROM pg_indexes
WHERE tablename='enrollments';


-- Test Query Using Partial Index

EXPLAIN SELECT * FROM enrollments WHERE grade IS NULL;

-- Since the enrollments table contains only a small
-- number of rows, PostgreSQL determines that a
-- Sequential Scan is more efficient than using
-- the partial index.
--
-- In larger databases with thousands of records,
-- PostgreSQL would typically use the partial index
-- for this query.