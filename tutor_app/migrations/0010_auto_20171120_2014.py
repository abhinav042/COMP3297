# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_app', '0009_auto_20171120_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]