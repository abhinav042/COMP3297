
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

def job():
    print ("I AM RUNNING EVERY 30 MINUTES")
    a = datetime.now()
    b = a - timedelta(minutes=30)
    session = Session.objects.get(id=50)
    session.status = 3
    session.tutor.wallet += session.tutor.salary
    session.save()
    with open('transaction_log.txt', 'w') as 
    #     f.write('This session ')
    # subject = "Payment Recieved"
    # from_email = "tutoria@admin.com"
    # to_email = "lundbc"
    # message =  "An amount of " + session.tutor.salary + " has been deposited to your wallet. Your Current balance is "+ session.tutor.wallet
    # send_mail(subject,message, from_email, to_email, fail_silently = False)

# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 1 # every 30 mins
    
#     schedule = Schedule(run_every_mins = RUN_EVERY_MINS)
#     code = 'session_app.my_cron_job'
    
#     def do(self):
#         # add the code which repeats here
#         print ("RUN\n")

# def my_scheduled_job():
#     print("RUN")

schedule.every(10).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)