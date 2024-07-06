from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_code = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=10)
    student_image = models.ImageField()
    grade_level = models.IntegerField()
    student_next_of_kin = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
