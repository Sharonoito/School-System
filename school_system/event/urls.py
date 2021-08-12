# from django.urls import path
from .views import register_event
# from django.conf import urls
# from django.conf.urls import url
# from django.conf.urls.static import static
# from django.conf import settings
from django import urls
from django.urls import path

urlpatterns=[
    path("register/",register_event,name="register_event"),
]






