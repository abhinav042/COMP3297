# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 02:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_app', '0016_auto_20171123_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 24, 2, 32, 32, 214527)),
        ),
    ]
