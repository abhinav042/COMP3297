# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 13:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session_app', '0002_auto_20171030_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='course',
        ),
    ]