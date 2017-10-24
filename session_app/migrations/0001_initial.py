# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_app', '0001_initial'),
        ('student_app', '0002_auto_20171023_2114'),
        ('tutor_app', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_time', models.DateTimeField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.Student')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_app.Tutor')),
            ],
        ),
    ]
