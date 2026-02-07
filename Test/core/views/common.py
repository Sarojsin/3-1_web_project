from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    """Home view - redirects based on user role"""
    if request.user.is_authenticated:
        if request.user.is_teacher():
            return redirect('teacher_dashboard')
        return redirect('student_dashboard')
    return redirect('login')
