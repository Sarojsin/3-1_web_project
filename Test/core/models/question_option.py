from django.db import models
from .question import Question


class QuestionOption(models.Model):
    """Option model for multiple choice and true/false questions"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'question_options'
        ordering = ['order']

    def __str__(self):
        return self.option_text[:50] + '...' if len(self.option_text) > 50 else self.option_text
