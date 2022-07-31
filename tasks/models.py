from abc import abstractclassmethod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AbstractTask(models.Model):
    task_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    task_title = models.CharField(max_length=1024, null=False, blank=False)
    task_description = models.TextField(blank=True, null=True)
    task_completed = models.BooleanField(default=False)
    class Meta:
        abstract = True 

class Task(AbstractTask):
    class Meta:
        abstract = False

