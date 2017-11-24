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
    url(r'^edit/', views.edit_profile, name='edit_profile'),
    url(r'^blockSession/$',views.blockSession, name='blockSession'),
    url(r'^timeSlots/$',views.timeSlots, name='timeSlots'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    url(r'^review/', views.review_list, name='review_list'),
    url(r'^tutor/$', views.tutor_list, name='tutor_list'),
    url(r'^tutor/(?P<tutor_id>[0-9]+)/$', views.tutor_detail, name='tutor_detail'),
    url(r'^tutor/(?P<tutor_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]
