from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    course_description = models.TextField()
    class_starting_time = models.TimeField()
    course_instructor = models.CharField(max_length=20)
     
    def __str__(self):
        return f"{self.course_name} {self.department}"
    
    