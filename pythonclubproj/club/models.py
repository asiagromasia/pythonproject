from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'

class Minutes(models.Model):
    minutestitle=models.CharField(max_length=255)
    meeting=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    meetingattendance=models.ManyToManyField(User)
    minutestext=models.CharField(max_length=500)
    minutesdate=models.DateField()

    def __str__(self):
        return self.minutesdate

    class Meta:
        db_table='minutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    resourcedate=models.DateField()
    resourcedateentered=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.CharField(max_length=255)

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'    
