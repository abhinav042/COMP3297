# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_auto_20171023_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='wallet',
            field=models.FloatField(default=0),
        ),
    ]