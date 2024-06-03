from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)