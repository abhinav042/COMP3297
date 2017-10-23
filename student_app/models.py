from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):

    user = models.OneToOneField(User,null=True)

    wallet = models.FloatField(null=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
