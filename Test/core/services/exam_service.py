from ..models import Test, Question, Answer, User


class ExamService:
    """Service for exam/test-taking operations"""
    
    @staticmethod
    def start_exam(test_id, student):
        """Start an exam for a student"""
        test = Test.objects.get(id=test_id, is_published=True)
        return {
            'test': test,
            'questions': test.questions.all(),
            'started_at': None  # Could track start time
        }
    
    @staticmethod
    def submit_answer(question_id, student, answer_text, is_correct=False):
        """Submit an answer for a question"""
        question = Question.objects.get(id=question_id)
        return Answer.objects.create(
            question=question,
            user=student,
            text=answer_text,
            is_correct=is_correct
        )
    
    @staticmethod
    def has_student_taken_test(test_id, student):
        """Check if student has already taken a test"""
        return Answer.objects.filter(
            question__test_id=test_id,
            user=student
        ).exists()
