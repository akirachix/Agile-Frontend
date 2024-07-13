from django.db import models
from course.models import Course

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    teacher_image = models.ImageField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    subject_specialisation = models.ForeignKey(Course, default=None, on_delete=models.CASCADE, related_name='subject_specialisation')
    bio = models.TextField()
    education_level = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    