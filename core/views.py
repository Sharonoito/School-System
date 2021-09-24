from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from event.models import Event

# Create your views here.

def home(request):
    student=Student.objects.count()
    trainers=Trainer.objects.count()
    courses=Course.objects.count()
    events=Event.objects.count()
    data={"students":student,"trainers":trainers,"courses":courses,"events":events,}
    return render(request,"homepage.html",data)
    
