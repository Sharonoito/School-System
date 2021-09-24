from django.db import models
from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from event.models import Event


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=("first_name","last_name","age")


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields=("first_name","last_name","email")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields=("course_name","course_code","trainer")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields=("event_name","event_link","venue")



      