# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def index(request):
    logout(request)
    return render(request,'base.html')
