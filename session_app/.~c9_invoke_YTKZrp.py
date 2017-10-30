# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .filter import SessionFilter
from session_app.models import Session
from student_app.models import Student
from django.contrib.auth.models import User

# Create your views here.

# class SessionDetailView(DetailView):

#     model = Session

#     def get_context_data(self, **kwargs):
#         context = super(SessionDetailView, self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context


def sessions(request):
    session_list = Session.objects.all()
    session_filter = SessionFilter(request.GET, queryset=session_list)
    s = User.objects.all()
    p
    return render(request, 'sessions.html', {'filter': session_filter,'user_id': user})
    
    
def book_session(request):
    session=Session.objects.get(id=request.GET.get('sess'))
    student=Student.objects.get(id=request.GET.get('stud'))
    session.student=student
    session.status=1
    session.save()
    
