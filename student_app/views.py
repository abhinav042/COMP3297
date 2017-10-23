from django.shortcuts import render
from models import Student

# Create your views here.

def index(request):
    student = Student.objects.create(
            full_name="Tom",
            username="ab42",
    )
    student.save()
    ## TO DO : RETURN A REQUEST TO ADD A USER