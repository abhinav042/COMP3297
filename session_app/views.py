# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .filter import SessionFilter
from session_app.models import Session
from student_app.models import Student
from django.contrib.auth.models import User
from django.shortcuts import redirect
from tutor_app.models import Tutor
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
    session=Session.objects.get(id=request.GET.get('sess'))
    user_id= request.user
    student=Student.objects.get(user=user_id)
    student.wallet = student.wallet - session.tutor.salary
    session.student=student
    session.status=1
    session.save()
    student.save()
    return redirect('/student_app/index')
    
def cancel_session(request):
    session=Session.objects.get(id=request.GET.get('sess'))
    user_id= request.user
    student=Student.objects.get(user=user_id)
    student.wallet = student.wallet + session.tutor.salary
    student.save()
    student=Student.objects.get(user=1)
    session.student=student
    session.status=0
    session.save()
    return redirect('/student_app/index')
    
def cronFuntion():
    a = datetime.now()
    b = a - timedelta(minutes=30)
    sessions = Session.objects.filter(session_time  = b)
    for session in sessions:
        session.status = 3
        session.tutor.wallet += session.tutor.salary
        subject = "Payment Recieved"
        from_email = "tutoria@admin.com"
        to_email = session.tutor.email
        message =  "An amount of " + session.tutor.salary + " has been deposited to your wallet. Your Current balance is "+ session.tutor.wallet
        send_mail(subject,message, from_email, to_email, fail_silently = False)
        
