from django.db import models
from student.models import Student


# Create your models here.
class Behaviour(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.TextField()

    def __str__(self):
        return self.event
