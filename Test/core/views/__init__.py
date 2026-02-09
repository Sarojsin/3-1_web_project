# Views
from .auth import login_view, logout_view, signup_view
from .teacher import teacher_dashboard, create_test, add_question, edit_question, view_test_questions, publish_test, delete_test, view_results
from .student import student_dashboard, take_test, view_student_result
from .common import home

__all__ = [
    'login_view', 'logout_view', 'signup_view',
    'teacher_dashboard', 'create_test', 'add_question', 'edit_question', 'view_test_questions', 'publish_test', 'delete_test', 'view_results',
    'student_dashboard', 'take_test', 'view_student_result',
    'home'
]
