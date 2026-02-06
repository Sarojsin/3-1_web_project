# Django Lab Project Structure

A Django-based testing/assessment platform with separate flows for teachers and students.

## Project Structure

```
Django_Lab_Project/
├── 📂 Test/                     # Project Configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── 📂 core/                     # Main Application
│   ├── __init__.py
│   ├── admin.py                # Admin registrations
│   ├── apps.py
│   ├── tests.py
│   │
│   ├── 📂 migrations/
│   │   └── __init__.py
│   │
│   ├── 📂 models/               # Database Models (logical split)
│   │   ├── __init__.py
│   │   ├── user.py              # Teacher / Student profile
│   │   ├── test.py               # Test / Exam
│   │   ├── question.py           # Questions
│   │   ├── answer.py             # Student answers
│   │   └── result.py             # Scores / Results
│   │
│   ├── 📂 views/                # View Logic (Flow-based)
│   │   ├── __init__.py
│   │   ├── auth.py               # Login / Logout
│   │   ├── teacher.py            # Teacher flow
│   │   ├── student.py            # Student flow
│   │   └── common.py             # Shared views
│   │
│   ├── 📂 urls/                 # URL Routing
│   │   ├── __init__.py
│   │   ├── auth.py               # /login /logout
│   │   ├── teacher.py            # /teacher/*
│   │   ├── student.py            # /student/*
│   │   └── common.py
│   │
│   ├── 📂 services/             # Business Logic
│   │   ├── __init__.py
│   │   ├── test_service.py       # Create / Publish tests
│   │   ├── exam_service.py       # Exam flow
│   │   └── result_service.py     # Score calculation
│   │
│   ├── 📂 templates/            # HTML Templates
│   │   ├── __init__.py
│   │   ├── base.html
│   │   ├── navbar.html
│   │   ├── login.html
│   │   │
│   │   ├── 📂 teacher/
│   │   │   ├── dashboard.html
│   │   │   ├── create_test.html
│   │   │   ├── add_question.html
│   │   │   └── results.html
│   │   │
│   │   ├── 📂 student/
│   │   │   ├── dashboard.html
│   │   │   ├── take_test.html
│   │   │   └── result.html
│   │
│   └── 📂 static/               # Static Files
│       ├── 📂 css/
│       ├── 📂 js/
│       └── 📂 images/
│
├── db.sqlite3
└── manage.py
```

## Quick Start

1. Install Django: `pip install django`
2. Run migrations: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`
4. Run server: `python manage.py runserver`

## User Roles

- **Teacher**: Create tests, add questions, view results
- **Student**: Take tests, view scores
