# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 10:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_app', '0012_auto_20171122_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='blocked_timeslots',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='courses',
        ),
    ]
