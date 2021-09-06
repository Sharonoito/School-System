from django.db import models
from django.urls import reverse
from django.utils import timezone
# import datetime


 #Create your models here.
class Event(models.Model):
    event_name=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    start_time=models.DateTimeField(default=timezone.now)
    end_time=models.DateTimeField(default=timezone.now)
    venue=models.CharField(max_length=50,default="AkiraChix")
    event_link=models.CharField(max_length=100)


    @property
    def get_html_url(self):
        url = reverse('calendar:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'





