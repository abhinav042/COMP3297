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
   # url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^session_list/(?P<tutor_id>\w+)$', views.session_list, name='session_list'),
    url(r'^index/update_wallet', views.update_wallet, name='update_wallet'),
    url(r'^warning/$', views.warning, name='warning'),
    url(r'^transactions/$', views.transactions, name='transactions'),
    #url(r'^timeSlots/$',views.timeSlots,name='timeslots'),
    url(r'^sort_price/$', views.sort_price, name='sort_price'),
    #url(r'^sort_rating/$', views.sort_rating, name='sort_rating'),
]
