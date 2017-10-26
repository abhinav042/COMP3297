from django.conf.urls import url
from session_app import views

# SET THE NAMESPACE!
app_name = 'session_app'

urlpatterns=[
   url(r'^sessions/$',views.sessions,name='sessions'),
    
]
