from django.conf.urls import url
from tutor_app import views

# SET THE NAMESPACE!
app_name = 'tutor_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^index/$',views.index,name='index'),
    url(r'^switch/$',views.switch,name='switch'),
    url(r'^profile/(?P<tutor_id>\w+)/$', views.profile, name='profile'),
    url(r'^edit/', views.edit_profile, name='edit_profile')
]
