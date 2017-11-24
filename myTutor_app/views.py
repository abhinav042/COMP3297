# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from myTutor_app.models import myTutor
from myTutor_app.forms import UserForm
import json
from django.http import JsonResponse

# Create your views here.
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =authenticate(username=username,password=password)
        

        if user:
            if user.is_active:
                login(request,user)
                return redirect('/myTutor_app/index')

            else:
                return HttpResponse('Not Registered as a Student')
        else:
            print('Someone Tried to login and failed')
            print('Username: {} and password: {}'.format(username,password))
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request,'myTutor_app/login.html',{})
 
@login_required      
def index(request):
    user_id = request.user
    my_Tutor = myTutor.objects.get(user = user_id)
    return render(request,'myTutor_app/index.html',{'mytutor':my_Tutor})
    
def update_wallet(request):
        user_id = request.user
        data = request.GET.get("value")
        print('hello')
        print(data)
        rand_json = { }
        mytutor = myTutor.objects.get(user = user_id)
        print(type(data))
        if mytutor.wallet < float(data):
            return JsonResponse({"error":"error"})
        else:
            mytutor.wallet -= float(data)
            mytutor.save()
            return JsonResponse(rand_json)

    
        
