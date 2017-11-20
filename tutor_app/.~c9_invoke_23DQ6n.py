from django.db import models
from django.contrib.auth.models import User
from course_app.models import Course

# Create your models here.
class Tutor(models.Model):

    user = models.OneToOneField(User,null=True)
    wallet = models.FloatField(null=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    bio = models.TextField(null=True)
    contracted = models.BooleanField(default=False)
    salary = models.FloatField(default=0)
    list_timeslots = models.ManyToManyField(D)
    blocked_timeslots = models.ManyToManyField(Timeslot, null=True)
    def __str__(self):
        return self.user.username
        
class Timeslot(models.Model):
    
    date_of_slot = models.DateField(null=True);
    time_of_slot = models.TimeField(null=True);