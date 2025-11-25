from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    STATUS_TODO = 'todo'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_DONE = 'done'

    STATUS_CHOICES = [
        (STATUS_TODO, 'To Do'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_DONE, 'Done'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_TODO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.owner})"
