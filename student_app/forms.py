from django import forms
from django.contrib.auth.models import User
from student_app.models import Student

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('profile_pic',)
