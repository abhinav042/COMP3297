# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 14:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_app', '0025_auto_20171124_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 24, 14, 6, 22, 207914)),
        ),
    ]
