from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models import User as CustomUser


def login_view(request):
    """Login view for both teachers and students"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_teacher():
                return redirect('teacher_dashboard')
            return redirect('student_dashboard')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid credentials'})
    return render(request, 'auth/login.html')


def signup_view(request):
    """Signup view for new teachers and students"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role', 'student')
        
        if password != confirm_password:
            return render(request, 'auth/signup.html', {'error': 'Passwords do not match'})
        
        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'auth/signup.html', {'error': 'Username already exists'})
        
        # Create user
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role
        )
        
        # Login the user
        login(request, user)
        
        if role == CustomUser.TEACHER:
            return redirect('teacher_dashboard')
        return redirect('student_dashboard')
    
    return render(request, 'auth/signup.html')


@login_required
def logout_view(request):
    """Logout view"""
    logout(request)
    return redirect('login')
