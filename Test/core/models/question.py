from django.db import models
from .test import Test


class Question(models.Model):
    """Question model for tests"""
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    question_type = models.CharField(
        max_length=20,
        choices=[
            ('multiple_choice', 'Multiple Choice'),
            ('true_false', 'True/False'),
            ('short_answer', 'Short Answer'),
        ],
        default='multiple_choice'
    )
    points = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.text[:50] + '...' if len(self.text) > 50 else self.text

    def get_answers(self):
        return self.answers.all()
