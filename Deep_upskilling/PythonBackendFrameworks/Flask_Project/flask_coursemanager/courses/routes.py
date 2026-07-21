from flask import Blueprint, jsonify, request
from extensions import db
from courses.models import Course

courses_bp = Blueprint(
    'courses',
    __name__,
    url_prefix='/api/courses'
)

def make_response_json(data, status_code=200):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


@courses_bp.route('/', methods=['GET'])
def get_courses():

    courses = Course.query.all()

    result = []

    for course in courses:
        result.append({
            "id": course.id,
            "name": course.name,
            "code": course.code,
            "credits": course.credits,
            "department_id": course.department_id
        })

    return jsonify(result)


@courses_bp.route('/', methods=['POST'])
def create_course():

    data = request.get_json()

    course = Course(
        name=data['name'],
        code=data['code'],
        credits=data['credits'],
        department_id=data['department_id']
    )

    db.session.add(course)
    db.session.commit()

    return jsonify({
        "message": "Course created successfully",
        "id": course.id
    }), 201
    
@courses_bp.route('/<int:id>', methods=['GET'])
def get_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({
            "error": "Course not found"
        }), 404

    return jsonify({
        "id": course.id,
        "name": course.name,
        "code": course.code,
        "credits": course.credits,
        "department_id": course.department_id
    })

@courses_bp.route('/<int:id>', methods=['PUT'])
def update_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({
            "error": "Course not found"
        }), 404

    data = request.get_json()

    course.name = data.get(
        'name',
        course.name
    )

    course.code = data.get(
        'code',
        course.code
    )

    course.credits = data.get(
        'credits',
        course.credits
    )

    db.session.commit()

    return jsonify({
        "message": "Course updated"
    })

@courses_bp.route('/<int:id>', methods=['DELETE'])
def delete_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({
            "error": "Course not found"
        }), 404

    db.session.delete(course)
    db.session.commit()

    return jsonify({
        "message": "Course deleted"
    })