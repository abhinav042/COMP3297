# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from course_app.models import Course, Subject

# Register your models here.
admin.site.register(Course)
admin.site.register(Subject)
