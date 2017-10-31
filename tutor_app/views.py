from django.shortcuts import render
from tutor_app.forms import UserForm , TutorForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from tutor_app.models import Tutor

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
