# Task 2: 

"""Separate Python Enviornment

Creation of Environment: python -m venv venv
Activate Environment: venv\Scripts\activate

Install Django

Open terminal: pip install django

Verify: python -m django --version


Create Django Project

Move to your working folder: cd C:\Users\ANNAPOORANI\OneDrive\Documents\GitHub\CTS-DNS-5.0-Exercises\Deepskilling\Module_4

Create project: django-admin startproject coursemanager

Move inside: cd coursemanager

Run server: python manage.py runserver

Open browser: http://127.0.0.1:8000 """

#FILE STRUCTURE

# settings.py - Stores project configuration and installed apps
# urls.py - Defines URL routes for the project
# wsgi.py - Entry point for WSGI deployment
# asgi.py - Entry point for ASGI deployment

""" Entire web application configuration.

Example: Course Management System

Reusable module inside a project.

    -- courses
    -- students
    -- faculty
    -- library

One project can contain multiple apps. """