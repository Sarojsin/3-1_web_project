from django.urls import path
from ..views import teacher_dashboard, create_test, add_question, edit_question, view_test_questions, publish_test, delete_test, view_results

urlpatterns = [
    path('teacher/dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('teacher/create-test/', create_test, name='create_test'),
    path('teacher/add-question/<int:test_id>/', add_question, name='add_question'),
    path('teacher/edit-question/<int:test_id>/<int:question_id>/', edit_question, name='edit_question'),
    path('teacher/view-questions/<int:test_id>/', view_test_questions, name='view_test_questions'),
    path('teacher/publish-test/<int:test_id>/', publish_test, name='publish_test'),
    path('teacher/delete-test/<int:test_id>/', delete_test, name='delete_test'),
    path('teacher/results/', view_results, name='view_results'),
]
