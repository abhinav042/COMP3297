from django.db import models
from django.contrib.auth.models import User

# Create your models here.
user = models.OneToOneField(User)

wallet = models.FloatField(default=0)
profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

def __str__(self):
    return self.user.username
