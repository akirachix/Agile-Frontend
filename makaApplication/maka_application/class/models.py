from django.db import models

# Create your models here.
class Class(models.Model):
      number_of_students = models.PositiveSmallIntegerField()
      class_name = models.CharField(max_length=20)
      capacity = models.PositiveSmallIntegerField()
      class_id = models.PositiveSmallIntegerField()    