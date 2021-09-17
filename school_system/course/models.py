from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=50)
    course_code=models.CharField(max_length=10)
    course_channel=models.CharField(max_length=20)
    trainer=models.CharField(max_length=20)
    description=models.TextField(max_length=500)
    course_email=models.EmailField(default=0)
    syllabus=CharField(max_length=20)
