from flask import Flask
from flask import request
from flask import Response

import requests

app = Flask(__name__)


@app.route(
    "/api/courses/<path:path>",
    methods=[
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ]
)
def course_gateway(path):

    response = requests.request(
        method=request.method,
        url=f"http://127.0.0.1:5001/api/courses/{path}",
        json=request.get_json(
            silent=True
        )
    )

    return Response(
        response.content,
        status=response.status_code,
        content_type=response.headers.get(
            "Content-Type"
        )
    )


@app.route(
    "/api/students/<path:path>",
    methods=[
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ]
)
def student_gateway(path):

    response = requests.request(
        method=request.method,
        url=f"http://127.0.0.1:5002/api/students/{path}",
        json=request.get_json(
            silent=True
        )
    )

    return Response(
        response.content,
        status=response.status_code,
        content_type=response.headers.get(
            "Content-Type"
        )
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)