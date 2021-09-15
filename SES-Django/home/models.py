from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    eid = models.CharField(max_length=100,null=True)
    event_name = models.CharField(max_length=50, null=True)
    date=models.CharField(max_length=50,null=True)    
    start_time=models.CharField(max_length=50,null=True)
    end_time=models.CharField(max_length=10,null=True)
    limit=models.IntegerField(null=True)
    destination=models.TextField(max_length=1000,null=True)
    is_event=models.BooleanField(default=True)
    
    def __str__(self):
        return self.eid

class Attendees(models.Model):
    eid = models.CharField(max_length=100,null=True)
    attendees_name = models.CharField(max_length=50, null=True)
    attendees_email=models.CharField(max_length=50,null=True)    
    attendees_phone=models.IntegerField(null=True)
    age=models.IntegerField(null=True)
    def __str__(self):
        return self.attendees_email
##(eventid,name,email,phone,age,gender)