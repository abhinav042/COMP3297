from django import forms
from django.contrib.auth.models import User
from student_app.models import Student

class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class Student(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('profile_pic')
