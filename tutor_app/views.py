from django.shortcuts import render
from tutor_app.forms import UserForm , TutorForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from tutor_app.models import Tutor, Review
from tutor_app.forms import EditProfileForm, EditUserForm, ReviewForm
import datetime
import json
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from session_app.models import Session
from django.shortcuts import get_object_or_404

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
        try:
            tutor = Tutor.objects.get(user=user)
        except:
            tutor=None
        if user:
            if tutor != None:
                login(request,user)
                return render(request,'tutor_app/index.html')

            else:
                return HttpResponse('Not Registered as a Tutor')
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
    date_array = []
    exist_session = []
    lock_slot = []
    time_range = 18
    elem_time = datetime.time(9, 00)
    time_delta = datetime.timedelta(minutes = 30)
    tutor = Tutor.objects.get(user=request.user)

    for i in range(time_range):
        temp_time = datetime.datetime.combine(datetime.date(1, 1, 1), elem_time)
        preset_time.append(elem_time)
        elem_time = (temp_time + time_delta).time()

    curr_date = datetime.datetime.now().date()

    date_delta = datetime.timedelta(days = 1)
    lock_time = datetime.datetime.now() + date_delta + time_delta*16
    if tutor.contracted == False:
        time_range = 9
        time_delta = datetime.timedelta(minutes = 60)
    for i in range(14):
        temp_date = datetime.datetime.combine(curr_date, datetime.time(1,1))
        date_array.append(curr_date.strftime("%d/%m/%y (%a)"))
        curr_date = (temp_date + date_delta).date()
    for i in range(time_range):
        curr_date = datetime.datetime.now().date()
        time_slot.append(preset_time[i].strftime("%H:%M"))
        for j in range(14):
            time_to_append = datetime.datetime.combine(curr_date, preset_time[i]).isoformat()
            if Session.objects.filter(session_time = time_to_append).filter(tutor = tutor).exists():
                session = Session.objects.filter(session_time = time_to_append).filter(tutor = tutor).get()
                exist_session.append(time_to_append)
                print("session found")
                if session.status == '2':
                    lock_slot.append(time_to_append)
            if datetime.datetime.combine(curr_date, preset_time[i]) <= lock_time:
                lock_slot.append(time_to_append)
            time_slot.append(time_to_append)
            temp_date = datetime.datetime.combine(curr_date, datetime.time(1,1))
            curr_date = (temp_date + date_delta).date()

    return render(request,'tutor_app/timeSlots.html',{'timeSlot':time_slot, 'date_array':date_array, 'exist_session':exist_session, 'lock_slot':lock_slot})

def blockSession(request):

    if request.method=='POST':
        user_id=request.user
        json_data=json.loads(request.POST['data'])
        for data in json_data:
            tutor = Tutor.objects.get(user=user_id)
            if Session.objects.filter(session_time = data['timeslot']).filter(tutor = tutor).exists():
                print(data['timeslot']+ " Session Exist")
                session = Session.objects.filter(session_time = data['timeslot']).filter(tutor = tutor).get()
                if data['status'] != 0:
                    print("Session deleted")
                    session.delete()
            else:
                if data['status'] == 0:
                    print(data['timeslot']+ " Session Created")
                    session = Session(tutor = tutor, session_time = data['timeslot'], status = 0)
                    session.save()

        messages.success(request, 'Your timeslot has been updated.')
        return  JsonResponse({'message': 'Timeslot Edit Saved'})

    
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

def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'tutor_app/review_list.html', context)
    
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'tutor_app/review_detail.html', {'review': review})

def tutor_list(request):
    tutor_list = Tutor.objects.order_by('last_name')
    context = {'tutor_list':tutor_list}
    return render(request, 'tutor_app/tutor_list.html',{'tutor_list':tutor_list})
    
def tutor_detail(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    return render(request, 'tutor_app/tutor_detail.html', {'tutor':tutor})

def add_review(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.tutor = tutor
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('tutor_app:tutor_detail', args=(tutor.id,)))

    return render(request, 'tutor_app/add_review.html', {'tutor': tutor, 'form': form})

