from django.db.models import base
from django.urls import path,include
from rest_framework import routers
from .views import CourseViewSet, EventViewSet, StudentViewSet, TrainerViewSet


router = routers.DefaultRouter()

router.register("students/",StudentViewSet,basename='students')
router.register("trainers/",TrainerViewSet,basename='trainers')
router.register("courses/",CourseViewSet,basename='courses')
router.register("events/",EventViewSet,basename='events')


urlpatterns=[
    path("",include(router.urls)),
    
   
]