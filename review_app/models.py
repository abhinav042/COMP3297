from __future__ import unicode_literals

from mongoengine import *

# Create your models here.

class Review(Document):
    created = DateTimeField()
    author = ReferenceField(Student)
    tutor = ReferenceField(Tutor)
    text = StringField(max_length=256)
    rating = IntField(min_value=1, max_value=6)