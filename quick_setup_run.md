# Quick Setup & Run Guide

## Prerequisites
- Python 3.8+
- Django 6.0+

## Setup Steps

### 1. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 2. Install Dependencies
```bash
pip install django
```

### 3. Reset Database (If starting fresh)
```bash
# Delete old database if exists
del db.sqlite3

# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### 4. Start Development Server
```bash
python manage.py runserver
```

### 5. Access the Application
- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Creating Accounts

### Option 1: Sign Up via Website
1. Go to http://127.0.0.1:8000/
2. Click "Sign Up" in the navbar
3. Fill in the form:
   - Username (unique)
   - Email
   - Password
   - Select role: Student or Teacher
4. Click "Create Account"
5. You'll be redirected to your dashboard based on your role

### Option 2: Create via Admin Panel (Recommended for Teachers)
1. Go to http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Under "Core" section, click "Users"
4. Click "Add User" or create custom users with Teacher role

## User Roles

### Teacher
- Create and manage tests
- Add questions to tests
- Publish/unpublish tests
- View student results

### Student
- View available tests
- Take tests
- View their results

## Testing the Application

### Teacher Workflow:
1. Sign up as Teacher or login via admin
2. Go to Dashboard
3. Click "Create Test"
4. Add questions to the test
5. Wait for students to take the test
6. View results

### Student Workflow:
1. Sign up as Student
2. View available tests on dashboard
3. Click "Take Test"
4. Submit answers
5. View results

## URL Patterns

| URL | View | Description |
|-----|------|-------------|
| / | home | Home page (redirects based on role) |
| /login/ | login_view | Login page |
| /logout/ | logout_view | Logout |
| /signup/ | signup_view | Sign up for new account |
| /teacher/dashboard/ | teacher_dashboard | Teacher dashboard |
| /teacher/create-test/ | create_test | Create new test |
| /teacher/add-question/<id>/ | add_question | Add questions |
| /teacher/results/ | view_results | View all results |
| /student/dashboard/ | student_dashboard | Student dashboard |
| /student/take-test/<id>/ | take_test | Take a test |
| /student/result/<id>/ | view_student_result | View result |

## Troubleshooting

### Database Migration Errors
```bash
del db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

### No Module Named Django
Activate virtual environment first:
```bash
.\venv\Scripts\activate
```

### Template Not Found
Make sure templates are in the correct location:
- `core/templates/auth/login.html`
- `core/templates/auth/signup.html`
- `core/templates/teacher/`
- `core/templates/student/`

## Project Structure

```
django_lab_project/
├── Test/                      # Django Project Settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                      # Main Application
│   ├── models/               # Database Models
│   │   ├── user.py           # Custom User (Teacher/Student)
│   │   ├── test.py           # Test model
│   │   ├── question.py       # Question model
│   │   ├── answer.py         # Answer model
│   │   └── result.py         # Result model
│   ├── views/                # Views
│   │   ├── auth.py           # Login/Logout/Signup
│   │   ├── teacher.py        # Teacher flows
│   │   └── student.py        # Student flows
│   ├── urls/                 # URL Routing
│   ├── services/             # Business Logic
│   ├── templates/            # HTML Templates
│   │   ├── auth/            # Login/Signup templates
│   │   ├── teacher/         # Teacher templates
│   │   └── student/         # Student templates
│   └── static/               # CSS/JS/Images
└── db.sqlite3               # SQLite Database
```
