# from os import CLD_CONTINUED
from django.db import models
# from django.db.models.base import Model
# from datetime import date
# from django.db.models.fields import CharField

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=20,default=None)
    last_name=models.CharField(max_length=20,default=None)
    age=models.PositiveSmallIntegerField(default=None)
    date_of_birth=models.DateField(null=True)
    student_id=models.CharField(max_length=20,null=True)
    email=models.EmailField(default=None,blank=True,null=True)
    gender_choice=((u'F',u'Female'),(u'M',u'Male'),(u'O','Other'))
    gender=models.CharField(max_length=10,choices=gender_choice,default=None,blank=True,null=True)
    nationality=models.CharField(max_length=20,default=None,blank=True,null=True)
    course=models.CharField(max_length=30,null=True,blank=True)
    admission_date=models.DateField(auto_now=True, null=True)
    student_image=models.ImageField(upload_to="images/",default=None,blank=True,null=True)
    medical_report=models.FileField(upload_to="files/",default=None,blank=True,null=True)
    student_phonenumber=models.CharField(max_length=15,default=None,blank=True,null=True)
    class_name=models.CharField(max_length=10,default=None,blank=True,null=True)
    academical_year=models.CharField(max_length=5, default="2021",blank=True,null=True)
    gurdian_name=models.CharField(max_length=50,default=None,blank=True,null=True)
    gurdian_phonenumber=models.CharField(max_length=15,default=None,blank=True,null=True)
    
    
  
  
  









    
