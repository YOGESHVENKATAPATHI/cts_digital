from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    {
        "id": 1,
        "name": "Python Programming"
    },
    {
        "id": 2,
        "name": "Machine Learning"
    }
]

@app.route("/api/courses/<int:course_id>")
def get_course(course_id):

    for course in courses:

        if course["id"] == course_id:
            return jsonify(course)

    return jsonify(
        {
            "error": "Course not found"
        }
    ), 404


if __name__ == "__main__":
    app.run(port=5001, debug=True)