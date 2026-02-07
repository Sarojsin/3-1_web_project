from ..models import Result, Answer, Question


class ResultService:
    """Service for result/score calculations"""
    
    @staticmethod
    def calculate_score(test_id, student):
        """Calculate the score for a student's test"""
        answers = Answer.objects.filter(
            question__test_id=test_id,
            user=student
        )
        
        score = sum(
            answer.question.points 
            for answer in answers 
            if answer.is_correct
        )
        
        total_points = sum(
            answer.question.points 
            for answer in answers
        )
        
        return score, total_points
    
    @staticmethod
    def save_result(test, student, score, total_points):
        """Save test result for a student"""
        result = Result.objects.create(
            test=test,
            student=student,
            score=score,
            total_points=total_points
        )
        result.calculate_percentage()
        result.save()
        return result
    
    @staticmethod
    def get_student_results(student):
        """Get all results for a student"""
        return Result.objects.filter(student=student)
    
    @staticmethod
    def get_test_results(test):
        """Get all results for a specific test"""
        return Result.objects.filter(test=test)
