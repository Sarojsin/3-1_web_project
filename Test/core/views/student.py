from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Test, Result


@login_required
def student_dashboard(request):
    """Student dashboard view"""
    if not request.user.is_student():
        return redirect('teacher_dashboard')
    
    available_tests = Test.objects.filter(is_published=True)
    completed_tests = Result.objects.filter(student=request.user)
    
    context = {
        'available_tests': available_tests,
        'completed_tests': completed_tests,
    }
    return render(request, 'student/dashboard.html', context)


@login_required
def take_test(request, test_id):
    """Take a test"""
    if not request.user.is_student():
        return redirect('teacher_dashboard')
    
    test = get_object_or_404(Test, id=test_id, is_published=True)
    questions = test.get_questions()
    
    if request.method == 'POST':
        # Process answers and calculate score
        score = 0
        total_points = 0
        
        for question in questions:
            total_points += question.points
            # Get answer from POST data and calculate score
            answer_text = request.POST.get(f'question_{question.id}')
            # Add scoring logic here
        
        # Create result
        result = Result.objects.create(
            test=test,
            student=request.user,
            score=score,
            total_points=total_points
        )
        result.calculate_percentage()
        result.save()
        
        return redirect('view_student_result', result_id=result.id)
    
    context = {
        'test': test,
        'questions': questions,
    }
    return render(request, 'student/take_test.html', context)


@login_required
def view_student_result(request, result_id):
    """View test result"""
    if not request.user.is_student():
        return redirect('teacher_dashboard')
    
    result = get_object_or_404(Result, id=result_id, student=request.user)
    context = {'result': result}
    return render(request, 'student/result.html', context)
