
from session_app.models import Session
import django_filters
from django.forms import ModelForm, DateTimeInput



class SessionFilter(django_filters.FilterSet):
    class Meta:
        model = Session
        fields = ['tutor']
        