# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0005_transaction_s'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_s',
            name='desc',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
