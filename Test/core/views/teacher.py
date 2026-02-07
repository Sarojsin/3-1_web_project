from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Test, User, Result


@login_required
def teacher_dashboard(request):
    """Teacher dashboard view"""
    if not request.user.is_teacher():
        return redirect('student_dashboard')
    
    tests = Test.objects.filter(created_by=request.user)
    total_students = User.objects.filter(role=User.STUDENT).count()
    total_tests = tests.count()
    published_tests = tests.filter(is_published=True).count()
    
    context = {
        'tests': tests,
        'total_students': total_students,
        'total_tests': total_tests,
        'published_tests': published_tests,
    }
    return render(request, 'teacher/dashboard.html', context)


@login_required
def create_test(request):
    """Create a new test"""
    if not request.user.is_teacher():
        return redirect('student_dashboard')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        duration = request.POST.get('duration_minutes')
        
        test = Test.objects.create(
            title=title,
            description=description,
            created_by=request.user,
            duration_minutes=int(duration)
        )
        return redirect('add_question', test_id=test.id)
    
    return render(request, 'teacher/create_test.html')


@login_required
def add_question(request, test_id):
    """Add questions to a test"""
    if not request.user.is_teacher():
        return redirect('student_dashboard')
    
    test = Test.objects.get(id=test_id, created_by=request.user)
    
    if request.method == 'POST':
        text = request.POST.get('question_text')
        question_type = request.POST.get('question_type')
        points = request.POST.get('points')
        
        question = test.questions.create(
            text=text,
            question_type=question_type,
            points=int(points)
        )
        # Add answer choices here
        return redirect('teacher_dashboard')
    
    context = {'test': test}
    return render(request, 'teacher/add_question.html', context)


@login_required
def view_results(request):
    """View all test results"""
    if not request.user.is_teacher():
        return redirect('student_dashboard')
    
    results = Result.objects.filter(test__created_by=request.user)
    context = {'results': results}
    return render(request, 'teacher/results.html', context)
