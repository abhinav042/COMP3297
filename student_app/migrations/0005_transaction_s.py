# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0004_student_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction_S',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(null=True)),
                ('pub_date', models.DateTimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.Student')),
            ],
        ),
    ]
