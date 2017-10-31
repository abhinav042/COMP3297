# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .filter import SessionFilter
from session_app.models import Session
from student_app.models import Student
from django.contrib.auth.models import User
from django.shortcuts import redirect

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
    # user_id= request.user
    # print(user_id)
    # student=Student.objects.get(user=user_id)
    # print(student.id)
    return render(request, 'sessions.html', {'filter': session_filter})
    
    
def book_session(request):
    session=Session.objects.get(id=request.GET.get('sess'))
    user_id= request.user
    student=Student.objects.get(user=user_id)
    session.student=student
    session.status=1
    session.save()
    return redirect('/student_app/index')
    
def cancel_session(request):
    session=Session.objects.get(id=request.GET.get('sess'))
    student=Student.objects.get(user=1)
    session.student=student
    session.status=0
    session.save()
    return redirect('/student_app/index')
