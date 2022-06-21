from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f'{self.title}'


class Task(models.Model):
    STATUS = (
        ('ACTIVE', 'active'),
        ('DONE', 'done'),
    )

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list')
    text = models.TextField(blank=True)
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default='ACTIVE',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}'

