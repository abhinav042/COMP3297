from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tutor(models.Model):

    user = models.OneToOneField(User,null=True)
    wallet = models.FloatField(null=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    bio = models.TextField(null=True)
    contracted = models.BooleanField(default=False)
    salary = models.FloatField(default=0)

    def __str__(self):
        return self.user.username