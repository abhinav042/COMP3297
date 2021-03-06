# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=10, null = True)
    course_name = models.CharField(max_length=50,null = True)

    def __str__(self):
        return self.course_id
        
class Subject(models.Model):
    subject_code = models.CharField(max_length=10, null = True)
    subject_name = models.CharField(max_length=50,null = True)

    def __str__(self):
        return self.subject_name