from django.db import models

# Create your models here.
class Event(models.Model):
    event_name=models.CharField(max_length=20)
    event_date=models.DateTimeField()
    start_And_end=models.TimeField()
    venue=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    event_link=models.CharField(max_length=50)




