from course.models import Course
from django.shortcuts import render,redirect
from .forms import CourseRegistrationForm
from .models import Course

# Create your views here.

def register_course(request):
    if request.method=="POST":
        form=CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)   
    else:
        form=CourseRegistrationForm()

    return render(request,"register_course.html",{"form":form})  


def course_list(request):
    courses=Course.objects.all()
    return render(request,"course_list.html",{"courses":courses})  


#Updating courses information
def edit_course(request,id):
    course=Course.objects.get(id=id)

    if request.method=="POST":
        form=CourseRegistrationForm(request.POST,instance=course)

        if form.is_valid():
            form.save()

    else:
        form=CourseRegistrationForm(instance=course)
    return render (request,"edit_trainer.html",{"form":form})


#Checking course profile
def course_profile(request,id):
    course=Course.objects.get(id=id)
    return render(request,"course_profile.html",{"course":course})   


#Deleting instance of a course
def delete_course(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect("course_list")     
    
