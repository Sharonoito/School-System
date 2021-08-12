# from os import CLD_CONTINUED
from django.db import models
# from django.db.models.base import Model
# from datetime import date
# from django.db.models.fields import CharField

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12,default=None)
    last_name=models.CharField(max_length=20,default=None)
    age=models.PositiveSmallIntegerField(default=None)
    date_of_birth=models.DateField(default=None)
    student_id=models.CharField(max_length=15,default=None)
    email=models.EmailField(default=None)
    gender_choice=((u'F',u'Female'),(u'M',u'Male'),(u'O','Other'))
    gender=models.CharField(max_length=10,choices=gender_choice,default=None)
    nationality=models.CharField(max_length=20,default=None)
    admission_date=models.DateField(default=None)
    student_image=models.ImageField(upload_to="images/",default=None)
    room_no=models.CharField(max_length=15,default=None)
    medical_report=models.FileField(upload_to="files/",default=None)
    student_phonenumber=models.CharField(max_length=15,default=None)
    class_name=models.CharField(max_length=10,default=None)
    city=models.CharField(max_length=15,default=None)
    academical_year=models.CharField(max_length=5, default="2021")
    gurdian_name=models.CharField(max_length=50,default=None)
    gurdian_phonenumber=models.CharField(max_length=15,default=None)
    
    
  
  
  









    
