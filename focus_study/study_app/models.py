from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class StudySession(models.Model): # type: ignore
    course = models.CharField(max_length=100)
    motivation = models.CharField(max_length=200)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.course} - {self.motivation}"
    
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_description = models.TextField()
    motivation = models.TextField()
    target_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    