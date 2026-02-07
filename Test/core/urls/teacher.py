from django.urls import path
from ..views import teacher_dashboard, create_test, add_question, view_results

urlpatterns = [
    path('teacher/dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('teacher/create-test/', create_test, name='create_test'),
    path('teacher/add-question/<int:test_id>/', add_question, name='add_question'),
    path('teacher/results/', view_results, name='view_results'),
]
