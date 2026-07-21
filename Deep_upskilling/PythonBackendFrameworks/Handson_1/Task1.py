"""
TASK 1

REQUEST-RESPONSE CYCLE

Browser
   |
GET /api/courses/
   |
URL Router (urls.py)
   |
View Function/Class
   |
Model
(Database Query)
   |
Response
   |
Browser


MIDDLEWARE

Middleware sits between request and response.

Examples:

1. AuthenticationMiddleware
   Identifies logged-in users.

2. SessionMiddleware
   Manages user sessions.


WSGI vs ASGI

WSGI:
- Synchronous
- One request at a time
- Traditional Django server

ASGI:
- Asynchronous
- Supports WebSockets
- Handles multiple requests efficiently

Django uses WSGI by default.

Use ASGI when:
- Building chat applications
- Real-time notifications
- WebSockets


MVC vs MVT

MVC:
Model
View
Controller

Django MVT:

Model -> Model
View -> Template
Controller -> Django View

Django View behaves like Controller.
Template behaves like View.
"""