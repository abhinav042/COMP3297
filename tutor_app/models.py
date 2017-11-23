from django.db import models
from django.contrib.auth.models import User
from course_app.models import Course
import numpy as np

# Create your models here.
class Timeslot(models.Model):
    
    date_of_slot = models.DateTimeField(null=True);
    #time_of_slot = models.TimeField(null=True);

class Tutor(models.Model):

    user = models.OneToOneField(User,null=True)
    first_name = models.CharField(max_length=30,null=True);
    last_name = models.CharField(max_length=30,null=True);
    wallet = models.FloatField(null=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    bio = models.TextField(null=True)
    contracted = models.BooleanField(default=False)
    salary = models.FloatField(default=0)
    #courses = models.ManyToManyField(Course, null=True)
    subject_tag = models.CharField(max_length=30,null=True)
    university = models.CharField(max_length=30,null=True)
    #blocked_timeslots = models.ManyToManyField(Timeslot, null=True)
    def __str__(self):
        return self.user.username
        
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
class Review(models.Model):
    
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    )
    
    tutor = models.ForeignKey(Tutor)
    user_name = models.CharField(max_length = 100)
    comment = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    rating = models.IntegerField(choices = RATING_CHOICES)
    