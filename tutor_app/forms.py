from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from tutor_app.models import Tutor, Review
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
        
class EditProfileForm(forms.ModelForm):
    class Meta():
        model = Tutor
        fields = (
            'first_name', 'last_name', 'profile_pic', 'bio',
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
            'password'
        )
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }
        