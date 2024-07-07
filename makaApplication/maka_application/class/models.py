from django.db import models
from course.models import Course


# Create your models here.
class Class(models.Model):
      number_of_students = models.PositiveSmallIntegerField()
      class_name = models.CharField(max_length=20)
      capacity = models.PositiveSmallIntegerField()
      class_id_taken = models.ForeignKey(Course, default=1, on_delete=models.CASCADE, related_name='course_id_taken')  
      
      def __str__(self):
        return f"{self.class_name}"
      