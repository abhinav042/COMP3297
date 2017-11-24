# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .filter import SessionFilter
from session_app.models import Session
from student_app.models import Student
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from tutor_app.models import Tutor
import datetime
from datetime import datetime,timedelta
from django.core.mail import send_mail

# Create your views here.

# class SessionDetailView(DetailView):

#     model = Session

#     def get_context_data(self, **kwargs):
#         context = super(SessionDetailView, self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context


def sessions(request):
    session_list = Session.objects.filter(status=0)
    session_filter = SessionFilter(request.GET,queryset=session_list)
    return render(request, 'sessions.html', {'filter': session_filter})
    
    
def book_session(request):
    tutor=Tutor.objects.get(id=request.GET['tutor'])
    user_id= request.user
    student=Student.objects.get(user=user_id)
    if student.wallet > tutor.salary:
        session=Session(tutor=tutor, session_time=request.GET['sess'], student= student, status = 1)
        #session=Session.objects.get(id=request.GET.get('sess'))
        commission_amount = session.tutor.salary * 0.05
        student.wallet = student.wallet - ((session.tutor.salary) + commission_amount) 
        session.save()
        student.save()
        
        return redirect('/student_app/index')
    else:
        messages.success(request, "You Dont have enough money for booking the session")
        return render(request, 'student_app/warning.html')
    
    
def cancel_session(request):
    session=Session.objects.get(id=request.GET.get('sess'))
    user_id= request.user
    now = datetime.now() + timedelta(hours = 32) 
    sess_time = datetime.strptime(session.session_time.strftime("%Y-%m-%dT%H:%M:%S"), "%Y-%m-%dT%H:%M:%S")
    if sess_time > now:
        print("YESSSS")
        student=Student.objects.get(user=user_id)
        commission_amount = session.tutor.salary * 0.05
        student.wallet = student.wallet + session.tutor.salary + commission_amount
        student.save()
        session.delete()
        return redirect('/student_app/index')
    else:
        print("NOOOO")
        messages.warning(request, "You cannot cancel the upcoming session!!")
        return render(request, 'student_app/warning.html')
    
