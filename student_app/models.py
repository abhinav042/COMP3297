from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,null=True)

    wallet = models.FloatField(default=0)
    phone = models.CharField(max_length=30,null=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
        
class Transaction_S(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.FloatField(null = True)
    pub_date = models.DateTimeField()
    desc = models.CharField(max_length=30,null=True)