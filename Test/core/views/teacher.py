from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Test, User, Result, Question, QuestionOption


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
        
        # Handle options for multiple choice and true/false
        if question_type in ['multiple_choice', 'true_false']:
            if question_type == 'true_false':
                # True/False questions have fixed options
                QuestionOption.objects.create(
                    question=question,
                    option_text='True',
                    is_correct=request.POST.get('correct_true') == 'on',
                    order=1
                )
                QuestionOption.objects.create(
                    question=question,
                    option_text='False',
                    is_correct=request.POST.get('correct_false') == 'on',
                    order=2
                )
            else:
                # Multiple choice - get options from form
                options = [
                    request.POST.get('option_a'),
                    request.POST.get('option_b'),
                    request.POST.get('option_c'),
                    request.POST.get('option_d'),
                ]
                correct_option = request.POST.get('correct_option')  # 'a', 'b', 'c', or 'd'
                
                for idx, option_text in enumerate(options, start=1):
                    if option_text:
                        QuestionOption.objects.create(
                            question=question,
                            option_text=option_text,
                            is_correct=correct_option == chr(96 + idx),  # 'a' -> 1, 'b' -> 2, etc.
                            order=idx
                        )
        
        return redirect('teacher_dashboard')
    
    context = {'test': test}
    return render(request, 'teacher/add_question.html', context)


@login_required
def edit_question(request, test_id, question_id):
    """Edit an existing question in a test"""
    if not request.user.is_teacher():
        return redirect('student_dashboard')

    question = get_object_or_404(
        Question,
        id=question_id,
        test__id=test_id,
        test__created_by=request.user
    )
    options = list(question.options.all().order_by('order'))

    if request.method == 'POST':
        text = request.POST.get('question_text')
        question_type = request.POST.get('question_type')
        points = request.POST.get('points')

        question.text = text
        question.question_type = question_type
        question.points = int(points)
        question.save()

        question.options.all().delete()

        if question_type in ['multiple_choice', 'true_false']:
            if question_type == 'true_false':
                QuestionOption.objects.create(
                    question=question,
                    option_text='True',
                    is_correct=request.POST.get('correct_true') == 'on',
                    order=1
                )
                QuestionOption.objects.create(
                    question=question,
                    option_text='False',
                    is_correct=request.POST.get('correct_false') == 'on',
                    order=2
                )
            else:
                options_input = [
                    request.POST.get('option_a'),
                    request.POST.get('option_b'),
                    request.POST.get('option_c'),
                    request.POST.get('option_d'),
                ]
                correct_option = request.POST.get('correct_option')

                for idx, option_text in enumerate(options_input, start=1):
                    if option_text:
                        QuestionOption.objects.create(
                            question=question,
                            option_text=option_text,
                            is_correct=correct_option == chr(96 + idx),
                            order=idx
                        )

        return redirect('view_test_questions', test_id=test_id)

    options_map = {1: '', 2: '', 3: '', 4: ''}
    correct_option = None
    correct_true = False
    correct_false = False

    if question.question_type == 'multiple_choice':
        for option in options:
            if option.order in options_map:
                options_map[option.order] = option.option_text
            if option.is_correct:
                correct_option = chr(96 + option.order)
    elif question.question_type == 'true_false':
        for option in options:
            if option.option_text.lower() == 'true':
                correct_true = option.is_correct
            elif option.option_text.lower() == 'false':
                correct_false = option.is_correct

    context = {
        'test': question.test,
        'question': question,
        'options_map': options_map,
        'correct_option': correct_option,
        'correct_true': correct_true,
        'correct_false': correct_false,
    }
    return render(request, 'teacher/edit_question.html', context)


@login_required
def view_test_questions(request, test_id):
    """View all questions in a test"""
    if not request.user.is_teacher():
        return redirect('student_dashboard')
    
    test = get_object_or_404(Test, id=test_id, created_by=request.user)
    questions = test.questions.all()
    
    context = {
        'test': test,
        'questions': questions,
    }
    return render(request, 'teacher/view_questions.html', context)


@login_required
def publish_test(request, test_id):
    """Publish a test so students can access it"""
    if not request.user.is_teacher():
        return redirect('student_dashboard')
    
    test = get_object_or_404(Test, id=test_id, created_by=request.user)
    
    if request.method == 'POST':
        test.is_published = True
        test.save()
    
    return redirect('teacher_dashboard')


@login_required
def delete_test(request, test_id):
    """Delete a test created by the teacher"""
    if not request.user.is_teacher():
        return redirect('student_dashboard')

    test = get_object_or_404(Test, id=test_id, created_by=request.user)

    if request.method == 'POST':
        test.delete()

    return redirect('teacher_dashboard')


@login_required
def view_results(request):
    """View all test results"""
    if not request.user.is_teacher():
        return redirect('student_dashboard')
    
    results = Result.objects.filter(test__created_by=request.user)
    context = {'results': results}
    return render(request, 'teacher/results.html', context)
