from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    teacher_image = models.ImageField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    subject_specialisation = models.CharField(max_length=30)
    bio = models.TextField()
    education_level = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    