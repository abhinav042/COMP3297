from django import forms
from django.contrib.auth.models import User
from tutor_app.models import Tutor

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')

class TutorForm(forms.ModelForm):
    class Meta():
        model = Tutor
        fields = ('profile_pic','bio','contracted','salary')
