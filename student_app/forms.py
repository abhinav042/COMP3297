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
        
class EditProfileForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = (
            'profile_pic', 'phone'
        )
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')
        
class EditUserForm(UserChangeForm):
    class Meta():
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )

class TutorFilter(django_filters.FilterSet):
    class Meta():
        model = Tutor
        fields = ['first_name','last_name','subject_tag','university','courses']

        
