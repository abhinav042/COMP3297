# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class myTutor(models.Model):
    user = models.OneToOneField(User,null=True)
    wallet = models.FloatField(default=0)
    
    def __str__(self):
        return self.user.username
        
class Transaction_M(models.Model):
    mytutor = models.ForeignKey(myTutor, on_delete=models.CASCADE)
    amount = models.FloatField(null = True)
    pub_date = models.DateTimeField()
    desc = models.CharField(max_length=30,null=True)
