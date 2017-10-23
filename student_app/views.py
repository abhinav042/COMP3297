from django.shortcuts import render
from student_app.forms import UserForm , StudentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'student_app/index.html')

@login_required
def special(request):
    return HttpResponse('You are logged in')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

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

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account Not Active')
        else:
            print('Someone Tried to login and failed')
            print('Username: {} and password: {}'.format(username,password))
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request,'student_app/login.html',{})
