# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_app', '0002_auto_20171024_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='salary',
            field=models.FloatField(default=0),
        ),
    ]
