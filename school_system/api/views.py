from django.http.request import QueryDict
from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from event.models import Event
from.serializers import StudentSerializer
from.serializers import TrainerSerializer
from.serializers import CourseSerializer
from.serializers import EventSerializer



# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    querySet=Trainer.objects.all()
    serializer_class=TrainerSerializer  
      
class CourseViewSet(viewsets.ModelViewSet):
    querySet=Course.objects.all()
    serializer_class=CourseSerializer 

class EventViewSet(viewsets.ModelViewSet):
    querySet=Event.objects.all()
    serializer_class=EventSerializer
                  

