# Models for the College Database

# STEP 75: Import Required Libraries
from sqlalchemy import (
Column,
Integer,
String,
Date,
ForeignKey,
Numeric,
create_engine
)

from sqlalchemy.orm import (
declarative_base,
relationship
)


# STEP 76: PostgreSQL Connection

DATABASE_URL = (
"postgresql+psycopg2://postgres:Ganesh36#$@localhost:5432/clg_db_orm"
)

engine = create_engine(DATABASE_URL,echo=True)

Base = declarative_base()


# STEP 77: Define ORM Models

# Department

class Department(Base):
    __tablename__ = "departments"
    
    department_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), nullable=False)
    hod_name = Column(String(100))
    budget = Column(Numeric(12, 2))
    
    students = relationship("Student", back_populates="department")
    professors = relationship("Professor", back_populates="department")
    courses = relationship("Course", back_populates="department")


# Student

class Student(Base):
    __tablename__ = "students"
    
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(15))

    date_of_birth = Column(Date)
    department_id = Column(Integer,ForeignKey("departments.department_id"))
    enrollment_year = Column(Integer)
    
    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment",back_populates="student")


# Course
class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(150), nullable=False)
    course_code = Column(String(20), unique=True)
    credits = Column(Integer)
    department_id = Column(Integer,ForeignKey("departments.department_id"))

    department = relationship("Department",back_populates="courses")

    enrollments = relationship("Enrollment",back_populates="course")


# Enrollment

class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True)
    student_id = Column(Integer,ForeignKey("students.student_id"))
    course_id = Column(Integer,ForeignKey("courses.course_id"))
    enrollment_date = Column(Date)
    grade = Column(String(2))
    
    student = relationship("Student",back_populates="enrollments")
    course = relationship("Course",back_populates="enrollments")


# Professor

class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True)
    prof_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    salary = Column(Numeric(10, 2))
    department = relationship("Department",back_populates="professors")


# STEP 78: Relationships Defined Above

# Student -> Department
# Course -> Department
# Professor -> Department
# Enrollment -> Student
# Enrollment -> Course


# STEP 79: Create All Tables

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("All ORM tables created successfully.")
