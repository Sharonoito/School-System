from django.conf.urls import url 
from django.urls  import path
from . import views


urlpatterns = [

    path("register/",views.register_event,name="register_event"),
    path("calendar/",views.CalendarView.as_view(),name="calendar"),
    path("event_list/",views.event_list,name="viewEvent"),
    path("event_edit/<int:id>/", views.edit_event, name='edit_event'),
    path("profile/<int:id>/",views.event_profile,name="event_profile"),
    path("delete/<int:id>/",views.delete_event,name="delete_event"),
    # path("edit/<int:id>/",views.event_edit,name="event_edit"),

]








