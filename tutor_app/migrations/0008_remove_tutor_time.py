# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_app', '0007_tutor_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='time',
        ),
    ]
