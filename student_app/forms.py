from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from student_app.models import Student
import django_filters
from tutor_app.models import Tutor

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('profile_pic',)
        
# class EditProfileForm(UserChangeForm):
#     class Meta():
#         model = Student
#         fields = (
#             'email',
#             'first_name',
#             'last_name',
#         )
        
class TutorFilter(django_filters.FilterSet):
    class Meta():
        model = User
        fields = ['first_name','last_name']

        
