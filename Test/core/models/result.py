from django.db import models
from .test import Test
from .user import User


class Result(models.Model):
    """Test result/scores model"""
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    score = models.FloatField(default=0.0)
    total_points = models.FloatField(default=0.0)
    percentage = models.FloatField(default=0.0)
    completed_at = models.DateTimeField(auto_now_add=True)
    is_passed = models.BooleanField(default=False)

    class Meta:
        db_table = 'results'

    def __str__(self):
        return f"{self.student.username} - {self.test.title}: {self.percentage}%"

    def calculate_percentage(self):
        if self.total_points > 0:
            self.percentage = (self.score / self.total_points) * 100
            self.is_passed = self.percentage >= 40  # Pass threshold
