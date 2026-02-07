from django.db import models
from .user import User


class Test(models.Model):
    """Test/Exam model"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tests')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    duration_minutes = models.IntegerField(default=60)

    class Meta:
        db_table = 'tests'

    def __str__(self):
        return self.title

    def get_questions(self):
        return self.questions.all()

    def get_total_questions(self):
        return self.questions.count()
