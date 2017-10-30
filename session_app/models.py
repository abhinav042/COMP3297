# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from student_app.models import Student
from tutor_app.models import Tutor
from course_app.models import Course
from django.views.generic.detail import DetailView
from django.utils import timezone

# Create your models here.
class Session(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session_time = models.DateTimeField(null=True)
    # 0=unavailable 1=available
    status = models.IntegerField(default=0)
    

    def __str__(self):
        return str(self.id)
        
# class SessionDetailView(DetailView):

#     model = Session

#     def get_context_data(self, **kwargs):
#         context = super(SessionDetailView, self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context

