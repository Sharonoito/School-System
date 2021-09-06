# from os import CLD_CONTINUED
from django.db import models
# from django.db.models.base import Model
# from django.db.models.fields import CharField

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=12,default=None)
    last_name=models.CharField(max_length=20,default=None)
    course=models.CharField(max_length=20,default=None)
    email=models.EmailField(default=0)
    national_id=models.CharField(max_length=15,default=None)
    contract=models.FileField(upload_to="files/",default=None)
    resume=models.FileField(upload_to="files/",default=None)
    salary=models.PositiveBigIntegerField(default=None)
    trainer_image=models.ImageField(upload_to="images/",default=None)
    gender_choice=((u'F',u'Female'),(u'M',u'Male'),(u'O','Other'))
    gender=models.CharField(max_length=10,choices=gender_choice,default=None)
    phonenumber=models.CharField(max_length=15,default=None)
    syllabus_relationship=models.CharField(max_length=20,default=None)
    course_name=models.CharField(max_length=20,default=None)
    course_code=models.CharField(max_length=5,default=None)
    company=models.CharField(max_length=20,default=None)
    joining_date=models.DateField(default=None)
