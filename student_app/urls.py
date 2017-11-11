from django.conf.urls import url
from student_app import views
from django.contrib.auth.views import password_reset,password_reset_done


# SET THE NAMESPACE!
app_name = 'student_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^index/$',views.index,name='index'),
    url(r'^switch/$',views.switch,name='switch'),
    url(r'^reset-password/$',password_reset,name='password_reset'),
    url(r'^reset-password/done/$',password_reset_done,name='password_reset_done'),
]
