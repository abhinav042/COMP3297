from django.conf.urls import url
from myTutor_app import views


app_name = 'myTutor_app'

urlpatterns=[
   url(r'^index/$',views.index,name='index'),
   url(r'^user_login/$',views.user_login,name='user_login'),
   url(r'^index/update_wallet/$',views.update_wallet,name='update_wallet'),
   url(r'^transactions/$',views.transactions,name='transactions')

]