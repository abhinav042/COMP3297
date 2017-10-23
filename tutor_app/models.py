from __future__ import unicode_literals

from mongoengine import *

# Create your models here.

class CourseId(EmbeddedDocument):
    course_id = StringField()
    course_time = ListField(DateTimeField())
    
class Student(Document):
    full_name  = StringField(max_length=30)
    username = StringField(max_length=30, unique=True)
    email = EmailField(max_length=30, unique=True)
    courses = EmbeddedDocumentListField(EmbeddedDocumentField(CourseId))
    contracted = BooleanField()
    salary = FloatField(default=0)
    bio = StringField()
    visible = BooleanField(default=True)
    wallet = FloatField()
    photo = StringField()
    password_reset_token = StringField()
    password_token_expiration = DateTimeField()