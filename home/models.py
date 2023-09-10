from django.db import models

# Create your models here.

class Task(models.Model):
    taskTitle = models.CharField(max_length=50, blank=False, null = False, unique=True)
    taskDesc = models.TextField(blank=False, null=False)
    time = models.DateTimeField()

    def __str__(self):
        return self.taskTitle