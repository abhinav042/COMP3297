from django.shortcuts import render
from tutor_app.forms import UserForm , TutorForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from tutor_app.models import Tutor
from tutor_app.forms import EditProfileForm, EditUserForm
import datetime
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from session_app.models import Session

# Create your views here.
def index(request):
    return render(request,'tutor_app/index.html')

def switch(request):
    logout(request)
    return redirect('/student_app/index')
    
def profile(request,tutor_id):
    tutor = Tutor.objects.get(id=tutor_id)
    return render(request,'tutor_app/profile.html',{'tutor':tutor})


@login_required
def user_logout(request):
    logout(request)
    return render(request,'tutor_app/index.html')

def register(request):
    registered =False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        tutor_form = TutorForm(data=request.POST)

        if user_form.is_valid() and tutor_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            tutor = tutor_form.save(commit=False)
            tutor.user = user

            if 'profile_pic' in request.FILES:
                tutor.profile_pic = request.FILES['profile_pic']

            tutor.save()

            registered = True

        else:
            print(user_form.errors,tutor_form.errors)

    else:
        user_form = UserForm()
        tutor_form = TutorForm()

    return render(request,'tutor_app/registration.html',
                            {'user_form':user_form,
                            'tutor_form':tutor_form,
                            'registered':registered}
                            )



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,'tutor_app/index.html')

            else:
                return HttpResponse('Account Not Active')
        else:
            print('Someone Tried to login and failed')
            print('Username: {} and password: {}'.format(username,password))
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request,'tutor_app/login.html',{})
        
@login_required      
def edit_profile(request):
    args = {}
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user.tutor)
        form2 = EditUserForm(request.POST, instance=request.user)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('/tutor_app/index')
    
    else:
        form = EditProfileForm(instance=request.user.tutor)
        form2 = EditUserForm(instance=request.user)
        args['form'] = form
        args['form2'] = form2
        return render(request, 'tutor_app/edit_profile.html', args)
        
def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta
            
def timeSlots(request):
    preset_time = []
    time_slot = []
    elem_time = datetime.time(9, 00)
    time_delta = datetime.timedelta(minutes = 30)
    for i in range(18):
        temp_time = datetime.datetime.combine(datetime.date(1, 1, 1), elem_time)
        preset_time.append(elem_time)
        elem_time = (temp_time + time_delta).time()
    
    curr_date = datetime.datetime.now().date()
    date_delta = datetime.timedelta(days = 1)
    for i in range(14):
        for j in range(18):
            time_to_append = datetime.datetime.combine(curr_date, preset_time[j]).isoformat()
            time_slot.append(time_to_append)
        temp_date = datetime.datetime.combine(curr_date, datetime.time(1,1))
        curr_date = (temp_date + date_delta).date()
    
    # end = start + timedelta(1)
    # print(end)
    # dts = [dt.strftime('%Y-%m-%d %H:%M ') for dt in 
    #   datetime_range(start, datetime(2017, 11, 22, 9+10),timedelta(minutes=30))]
       
    ## returning timeslot array to the template
    return render(request,'tutor_app/timeSlots.html',{'timeSlot':time_slot})

def blockSession(request):
    timeSlot = request.GET.get("time")
    user_id=request.user
    tutor = Tutor.objects.get(user=user_id)
    session = Session(tutor = tutor, session_time = timeSlot, status = 1)
    session.save()
    
    
    
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
