
from django_cron import CronJobBase, Schedule
import schedule
import time 
from django.shortcuts import render
from session_app.models import Session
from student_app.models import Student
from django.contrib.auth.models import User
from django.shortcuts import redirect
from tutor_app.models import Tutor
from datetime import datetime,timedelta
from django.core.mail import send_mail
from myTutor_app.models import myTutor


def job():
    print ("I AM RUNNING EVERY 30 MINUTES")
    user_id = User.objects.get(username = 'MyTutor')
    mytutor = myTutor.objects.get(user=user_id)
    a = datetime.now()
    b = a - timedelta(minutes=30)
    sessions = Session.objects.filter(session_time = b)
    for session in sessions:
        session.status = 3
        tutor_id = session.tutor
        student_id = session.student
        tutor_id.wallet += tutor_id.salary
        session.save()
        tutor_id.save()
        mytutor.wallet += session.tutor.salary * 0.05
        mytutor.save()
        subject = "Successfully Completed Payment"
        from_email = "tutoria@admin.com"
        tutor_email = tutor_id.user.email
        to_email = [tutor_email]
        message =  "An amount of " + str(tutor_id.salary) + " has been added to your wallet. Your Current balance is "+ str(tutor_id.wallet)
        send_mail(subject,message, from_email, to_email, fail_silently = False)
        
        subject_s = "Review your tutor"
        from_email_s = "tutoria@admin.com"
        student_email = student_id.user.email
        to_email_s = [student_email]
        message_s =  "Review the tutor here ->   http://127.0.0.1:8000/tutor_app/tutor/" + str(tutor_id.id)+"/add_review"
        send_mail(subject_s,message_s, from_email_s, to_email_s, fail_silently = False)

schedule.every(10).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)