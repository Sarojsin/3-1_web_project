from ..models import Test, Question


class TestService:
    """Service for test-related operations"""
    
    @staticmethod
    def create_test(title, description, created_by, duration_minutes=60):
        """Create a new test"""
        return Test.objects.create(
            title=title,
            description=description,
            created_by=created_by,
            duration_minutes=duration_minutes
        )
    
    @staticmethod
    def publish_test(test_id):
        """Publish a test"""
        test = Test.objects.get(id=test_id)
        test.is_published = True
        test.save()
        return test
    
    @staticmethod
    def get_teacher_tests(teacher):
        """Get all tests created by a teacher"""
        return Test.objects.filter(created_by=teacher)
    
    @staticmethod
    def get_published_tests():
        """Get all published tests"""
        return Test.objects.filter(is_published=True)
