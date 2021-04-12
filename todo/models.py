from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UserType(models.TextChoices):
    STUDENT = 'STUD', 'Student'
    TEACHER = 'TEACH', 'Teacher'
    ADMINISTRATOR = 'ADMIN', 'Administrator'


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=5,
        choices=UserType.choices,
        default=UserType.STUDENT,
    )

    # student = models.BooleanField(default=True)
    # teacher = models.BooleanField(default=False)