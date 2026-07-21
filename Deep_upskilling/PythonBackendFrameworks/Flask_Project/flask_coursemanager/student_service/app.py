from flask import Flask
from flask import jsonify
from flask import request

import requests

app = Flask(__name__)


@app.route(
    "/api/students/<int:student_id>/enroll",
    methods=["POST"]
)
def enroll_student(student_id):

    data = request.get_json()

    course_id = data.get("course_id")

    try:

        response = requests.get(
            f"http://127.0.0.1:5001/api/courses/{course_id}"
        )

    except requests.exceptions.ConnectionError:

        return jsonify(
            {
                "error":
                "Course Service unavailable"
            }
        ), 503

    if response.status_code != 200:

        return jsonify(
            {
                "error":
                "Course does not exist"
            }
        ), 404

    return jsonify(
        {
            "student_id": student_id,
            "course_id": course_id,
            "message":
            "Enrollment successful"
        }
    )
    

if __name__ == "__main__":
    app.run(port=5002, debug=True)