# URL Configuration
from .auth import urlpatterns as auth_urlpatterns
from .teacher import urlpatterns as teacher_urlpatterns
from .student import urlpatterns as student_urlpatterns
from .common import urlpatterns as common_urlpatterns

urlpatterns = auth_urlpatterns + teacher_urlpatterns + student_urlpatterns + common_urlpatterns
