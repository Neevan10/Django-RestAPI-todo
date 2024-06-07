from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    #id=models.BigAutoField(primary_key=True)
    task=models.CharField(max_length=180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task    