# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 21:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=b'profile_pics'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='wallet',
            field=models.FloatField(null=True),
        ),
    ]
