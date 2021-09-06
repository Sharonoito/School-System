from django.urls import path
from.views import delete_trainer, register_trainer
# from django.conf import urls
# from django.conf.urls import url
# from django.conf.urls.static import static
from django.conf import settings
from .views import register_trainer,trainer_list,edit_trainer,trainer_profile,delete_trainer

urlpatterns=[
    path("register/",register_trainer,name="register_trainer"),
    path("list/",trainer_list,name="trainer_list"),
    path("edit/<int:id>/",edit_trainer,name="edit_trainer"),
    path("profile/<int:id>/",trainer_profile,name="trainer_profile"),
    path("delete/<int:id>/",delete_trainer,name="delete_trainer"),
]


