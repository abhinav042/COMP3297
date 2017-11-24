# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from student_app.models import Student
from tutor_app.models import Tutor
from course_app.models import Course
from django.views.generic.detail import DetailView
from django.utils import timezone
from django_cron import CronJobBase, Schedule

# Create your models here.
class Session(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
   #course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session_time = models.DateTimeField(null=True)
  
    status = models.IntegerField(default=0)
    
    #0 = available
    #1 = booked
    #2 = blocked
    #3 = passed
    

    def __str__(self):
        return str(self.id)
        
# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 1 # every 30 mins
    
#     schedule = Schedule(run_every_mins = RUN_EVERY_MINS)
#     code = 'session_app.my_cron_job'
    
#     def do(self):
#         # add the code which repeats here
#         print ("RUN\n")dja
        
# class SessionDetailView(DetailView):

#     model = Session

#     def get_context_data(self, **kwargs):
#         context = super(SessionDetailView, self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context
