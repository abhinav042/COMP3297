# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class myTutor(models.Model):
    user = models.OneToOneField(User,null=True)
    wallet = models.FloatField(default=0)
