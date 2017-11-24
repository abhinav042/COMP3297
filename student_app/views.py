from django.shortcuts import render
from student_app.forms import UserForm , StudentForm,TutorFilter
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from session_app.models import Session
from student_app.models import Student
from django.shortcuts import redirect
from django.contrib.auth.forms import UserChangeForm
from tutor_app.models import Tutor
from django.contrib.auth.models import User
from student_app.forms import EditProfileForm
from student_app.forms import EditUserForm
from django.http import JsonResponse
from datetime import datetime,timedelta
from django.contrib.messages import get_messages
import datetime
import json
import unicodedata
from tutor_app.models import Timeslot
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def index(request):
    storage = get_messages(request)
    print("STorage")
    for message in storage:
        print("why?")
        print(message)
    user_id=request.user
    # student_id=Student.objects.get(user=user_id)p
    # session=Session.objects.filter(student=student_id)
    # print(session)
    try:
        student_id=Student.objects.get(user=user_id)
        print(student_id)
        
    except:
        student_id= None
    if student_id != None:    
        try:
            session = Session.objects.filter(student=student_id)
            print (session)
            return render(request,'student_app/index.html',{'sessions':session})
        except Session.DoesNotExist:
            session = None
            print(session)
    return render(request,'student_app/index.html', {'messages':storage})

def switch(request):
    logout(request)
    return redirect('/tutor_app/index')

@login_required
def user_logout(request):
    logout(request)
    return render(request,'student_app/index.html')

def register(request):
    registered =False
            
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        student_form = StudentForm(data=request.POST)

        if user_form.is_valid() and student_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            student = student_form.save(commit=False)
            student.user = user

            if 'profile_pic' in request.FILES:
                student.profile_pic = request.FILES['profile_pic']

            student.save()

            registered = True

        else:
            print(user_form.errors,student_form.errors)

    else:
        user_form = UserForm()
        student_form = StudentForm()

    return render(request,'student_app/registration.html',
                            {'user_form':user_form,
                            'student_form':student_form,
                            'registered':registered}
                            )

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =authenticate(username=username,password=password)
        try:
            student = Student.objects.get(user=user)
        except:
            student= None

        if user:
            if student != None:
                login(request,user)
                return redirect('/student_app/index')

            else:
                return HttpResponse('Not Registered as a Student')
        else:
            print('Someone Tried to login and failed')
            print('Username: {} and password: {}'.format(username,password))
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request,'student_app/login.html',{})
        
@login_required
def session_list(request,tutor_id):
    tutor = Tutor.objects.get(id=tutor_id)
    student=Student.objects.get(user=request.user)
    blocked_session = Session.objects.values_list('session_time','student_id').filter(tutor = tutor).filter(status = 2).all()
    booked_session = Session.objects.values_list('session_time','student_id').filter(tutor = tutor).filter(status = 1).all()
    booked_list = []
    blocked_list = []
    self_booked = []
    booked_day = []
    for session in blocked_session:
        blocked_list.append(session[0].strftime("%Y-%m-%dT%H:%M:%S"))
    for session in booked_session:
        booked_list.append(session[0].strftime("%Y-%m-%dT%H:%M:%S"))
        print(student.id)
        if (student.id == session[1]):
            self_booked.append(session[0].strftime("%Y-%m-%dT%H:%M:%S"))
            booked_day.append(session[0].strftime("%Y-%m-%d"))
    preset_time = []
    time_slot = []
    time_array = []
    date_array = []
    date_list = []
    lock_slot = []
    time_range = 18
    elem_time = datetime.time(9, 00)
    time_delta = datetime.timedelta(minutes = 30)

    

    curr_date = datetime.datetime.now().date()

    date_delta = datetime.timedelta(days = 1)
    lock_time = datetime.datetime.now() + date_delta + time_delta*16
    if tutor.contracted == False:
        time_range = 9
        time_delta = datetime.timedelta(minutes = 60)
    for i in range(time_range):
        temp_time = datetime.datetime.combine(datetime.date(1, 1, 1), elem_time)
        preset_time.append(elem_time)
        time_array.append(elem_time.strftime("%H:%M:%S"))
        elem_time = (temp_time + time_delta).time()
    for i in range(7):
        temp_date = datetime.datetime.combine(curr_date, datetime.time(1,1))
        date_array.append(curr_date.strftime("%Y-%m-%d"))
        date_list.append(curr_date.strftime("%d/%m/%y (%a)"))
        curr_date = (temp_date + date_delta).date()
    for i in range(time_range):
        curr_date = datetime.datetime.now().date()
        time_slot.append(preset_time[i].strftime("%H:%M"))
        for j in range(7):
            time_to_append = datetime.datetime.combine(curr_date, preset_time[i]).isoformat()
            if datetime.datetime.combine(curr_date, preset_time[i]) <= lock_time:
                lock_slot.append(time_to_append)
            time_slot.append(time_to_append)
            temp_date = datetime.datetime.combine(curr_date, datetime.time(1,1))
            curr_date = (temp_date + date_delta).date()

    return render(request, 'student_app/session_list.html', {'tutor_id':tutor_id,'self_booked':self_booked,'time_array':time_array,'date_list':date_list,'date_array':date_array, 'blocked_session_list': blocked_list,'booked_day':booked_day, 'booked_session_list': booked_list, 'lock_slot': lock_slot})
  
@login_required      
def edit_profile(request):
    args = {}
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user.student)
        form2 = EditUserForm(request.POST, instance=request.user)
        if form.is_valid() and form2.is_valid():
            form_extend = form.save(commit=False)

            if 'profile_pic' in request.FILES:
                form_extend.profile_pic = request.FILES['profile_pic']

            form_extend.save()
            form2.save()
            return redirect('/student_app/index')
    
    else:
        form = EditProfileForm(instance=request.user.student)
        form2 = EditUserForm(instance=request.user)
        args['form'] = form
        args['form2'] = form2
        return render(request, 'student_app/edit_profile.html', args)
        
def view_tutors(request):
    tutor_list = Tutor.objects.filter(active = True)
    tutor_filter = TutorFilter(request.GET,queryset=tutor_list)
    return render(request, 'student_app/tutor_list.html', {'filter': tutor_filter})
    
def validate_username(request):
    date = request.GET.get('username', None)
    datetime_object = datetime.datetime.strptime(date, '%b %d %Y %I:%M%p')
    timeslot = Timeslot(date_of_slot = datetime_object)
    timeslot.save()
    data={
        'haha':True
    }
    return JsonResponse(data)
    
    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was changed successfully')
            return redirect('change_password')
        else:
            messages.error(request, 'ERROR > ')
        
    else: 
        form = PasswordChangeForm(request.user)
    return render(request, 'student_app/change_password.html', {
        'form': form
    })
    
def update_wallet(request):
        user_id = request.user
        data = request.GET.get("value")
        print('hello')
        print(data)
        rand_json = { }
        student = Student.objects.get(user = user_id)
        print(type(data))
        student.wallet += float(data)
        student.save()
        return JsonResponse(rand_json)

# def datetime_range(start, end, delta):
#     current = start
#     while current < end:
#         yield current
#         current += delta
            
# def timeSlots(request):
#     dts = [dt.strftime('%Y-%m-%d T%H:%M Z') for dt in 
#       datetime_range(datetime.datetime.now), datetime(2016, 9, 1, 9+12), 
#       timedelta(minutes=30))]
#     return render(request,'tutor_app/timeSlots.html',{'timeSlot':dts})

def warning(request):
    return render(request, 'student_app/warning.html')