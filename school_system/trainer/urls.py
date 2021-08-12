from django.urls import path
from.views import register_trainer
from django.conf import urls
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path("register/",register_trainer,name="register_trainer"),
]
