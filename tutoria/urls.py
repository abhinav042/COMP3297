"""tutoria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from start_app import views
from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm,password_reset_complete
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^student_app/',include('student_app.urls')),
    url(r'^myTutor_app/',include('myTutor_app.urls')),
    url(r'^tutor_app/',include('tutor_app.urls')),
    url(r'^session_app/',include('session_app.urls')),
    url(r'^reset-password/$',password_reset,name='password_reset'),
    url(r'^reset-password/done/$',password_reset_done,name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm,name='password_reset_confirm'),
    url(r'^reset-password/complete/$',password_reset_complete,name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
