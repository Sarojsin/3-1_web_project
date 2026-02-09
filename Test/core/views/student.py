from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from ..models import Test, Result, Question, QuestionOption, Answer


@login_required
def student_dashboard(request):
    """Student dashboard view"""
    if not request.user.is_student():
        return redirect('teacher_dashboard')
    
    # Show published tests that students can take
    available_tests = Test.objects.filter(is_published=True)
    completed_tests = Result.objects.filter(student=request.user)
    
    # Get tests already taken by student
    taken_test_ids = completed_tests.values_list('test_id', flat=True)
    available_tests = available_tests.exclude(id__in=taken_test_ids)
    
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
    questions = test.questions.all()
    
    # Check if student has already taken this test
    existing_result = Result.objects.filter(test=test, student=request.user).first()
    if existing_result:
        return redirect('view_student_result', result_id=existing_result.id)
    
    if request.method == 'POST':
        score = 0
        total_points = 0
        
        for question in questions:
            total_points += question.points
            
            if question.question_type in ['multiple_choice', 'true_false']:
                # Get selected option
                selected_option_id = request.POST.get(f'question_{question.id}')
                if selected_option_id:
                    selected_option = get_object_or_404(QuestionOption, id=selected_option_id)
                    is_correct = selected_option.is_correct
                    answer_text = selected_option.option_text
                else:
                    is_correct = False
                    answer_text = ''
            else:
                # Short answer - student types their answer
                answer_text = request.POST.get(f'question_{question.id}', '')
                is_correct = False  # Will be graded manually
            
            # Save the answer
            Answer.objects.create(
                question=question,
                user=request.user,
                text=answer_text,
                is_correct=is_correct
            )
            
            if is_correct:
                score += question.points
        
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
    answers = Answer.objects.filter(question__test=result.test, user=request.user)
    
    context = {
        'result': result,
        'answers': answers,
    }
    return render(request, 'student/result.html', context)
