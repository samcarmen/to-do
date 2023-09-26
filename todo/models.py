from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    last_login_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    target_date = models.DateTimeField()
