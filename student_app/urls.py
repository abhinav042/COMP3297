from django.conf.urls import url
from student_app import views
from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm,password_reset_complete


# SET THE NAMESPACE!
app_name = 'student_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^index/$',views.index,name='index'),
    url(r'^switch/$',views.switch,name='switch'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^view_tutors/$',views.view_tutors,name='view_tutors'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^password/$', views.change_password, name='change_password')
    #url(r'^timeSlots/$',views.timeSlots,name='timeslots'),
]
