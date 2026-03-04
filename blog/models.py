from django.db import models
from django.contrib.auth.models import User



class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( unique=True)
    question = models.TextField()
    answer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    answer_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

