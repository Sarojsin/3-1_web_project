from django.db import models
from .question import Question
from .user import User


class Answer(models.Model):
    """Student answer model"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'answers'

    def __str__(self):
        return f"{self.user.username}'s answer to: {self.question.text[:30]}"
