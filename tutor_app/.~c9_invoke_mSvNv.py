from django import forms
from django.contrib.auth.models import User
from tutor_app.models import Tutor
from django.contrib.auth.forms import UserChangeForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class TutorForm(forms.ModelForm):
    class Meta():
        model = Tutor
        fields = ('first_name','last_name','profile_pic','bio','contracted','salary')
        
class EditProfileForm(UserChangeForm):
    class Meta():
        model = Tutor
        fields = (
            'wallet',
            'profile_pic'
        )
        
class EditUserForm(UserChangeForm):
    class Meta():
        model = User
        fields = (
            'email',
            'password'
        )
