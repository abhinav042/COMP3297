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
from tutor_app.models import Transaction_T
from student_app.models import Transaction_S

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
    student_id=Student.objects.get(user=user_id)
    if student_id.wallet > tutor.salary:
        session=Session(tutor=tutor, session_time=request.GET['sess'], student= student_id, status = 1)
        #session=Session.objects.get(id=request.GET.get('sess'))
        commission_amount = session.tutor.salary * 0.05
        amt_deducted = session.tutor.salary + commission_amount
        student_id.wallet = student_id.wallet - amt_deducted 
        session.save()
        student_id.save()
        transaction = Transaction_S(student = student_id, amount = -amt_deducted, pub_date = datetime.now(), desc="Book Session")
        transaction.save()
        
        subject = "Successfully Completed Payment"
        from_email = "tutoria@admin.com"
        student_email = user_id.email
        to_email = [student_email]
        message =  "An amount of " + str(session.tutor.salary) + " has been deducted from your wallet. Your Current balance is "+ str(session.student.wallet)
        send_mail(subject,message, from_email, to_email, fail_silently = False)

        subject_T = "Time slot Booked"
        from_email_T = "tutoria@admin.com"
        tutor_email = tutor.user.email
        to_email_T = [tutor_email]
        message_T =  user_id.first_name + " has booked a session with you. Session Details -> "+ str(session.session_time)
        send_mail(subject_T,message_T, from_email_T, to_email_T, fail_silently = False)

        
        return redirect('/student_app/index')
    else:
        messages.success(request, "You Dont have enough money for booking the session")
        return render(request, 'student_app/warning.html')
    
    
def cancel_session(request):
    session=Session.objects.get(id=request.GET.get('sess'))
    tutor_id = session.tutor
    user_id= request.user
    now = datetime.now() + timedelta(hours = 32) 
    sess_time = datetime.strptime(session.session_time.strftime("%Y-%m-%dT%H:%M:%S"), "%Y-%m-%dT%H:%M:%S")
    if sess_time > now:
        print("YESSSS")
        student_id=Student.objects.get(user=user_id)
        commission_amount = session.tutor.salary * 0.05
        student_id.wallet = student_id.wallet + session.tutor.salary + commission_amount
        student_id.save()
        amt_added = session.tutor.salary + commission_amount
        transaction = Transaction_S(student = student_id, amount = amt_added, pub_date = datetime.now(), desc = "Cancel Session")
        transaction.save()
        session.delete()
        
        subject = "Your money has been refunded"
        from_email = "tutoria@admin.com"
        student_email = user_id.email
        to_email = [student_email]
        message =  "An amount of " + str(session.tutor.salary) + " has been refunded to your wallet. Your Current balance is "+ str(session.student.wallet)
        send_mail(subject,message, from_email, to_email, fail_silently = False)

        subject_T = "Time slot Cancelled"
        from_email_T = "tutoria@admin.com"
        tutor_email = tutor_id.user.email
        to_email_T = [tutor_email]
        message_T =  user_id.first_name + " has cancelled a session with you. Session Details -> "+ str(session.session_time)
        send_mail(subject_T,message_T, from_email_T, to_email_T, fail_silently = False)
        
        return redirect('/student_app/index')
    else:
        print("NOOOO")
        messages.warning(request, "You cannot cancel the upcoming session!!")
        return render(request, 'student_app/warning.html')
    
