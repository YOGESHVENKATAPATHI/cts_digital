from extensions import db


class Department(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    head_of_dept = db.Column(
        db.String(100)
    )

    budget = db.Column(
        db.Float
    )

    courses = db.relationship(
        'Course',
        back_populates='department'
    )

    def __repr__(self):
        return self.name


class Course(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    code = db.Column(
        db.String(20),
        unique=True
    )

    credits = db.Column(
        db.Integer
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey('department.id')
    )

    department = db.relationship(
        'Department',
        back_populates='courses'
    )

    def __repr__(self):
        return self.name


class Student(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    first_name = db.Column(
        db.String(50)
    )

    last_name = db.Column(
        db.String(50)
    )

    email = db.Column(
        db.String(100),
        unique=True
    )

    enrollment_year = db.Column(
        db.Integer
    )


class Enrollment(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey('student.id')
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey('course.id')
    )

    grade = db.Column(
        db.String(5)
    )