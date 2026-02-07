from django.urls import path
from ..views import student_dashboard, take_test, view_student_result

urlpatterns = [
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('student/take-test/<int:test_id>/', take_test, name='take_test'),
    path('student/result/<int:result_id>/', view_student_result, name='view_student_result'),
]
