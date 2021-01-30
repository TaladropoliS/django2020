from __future__ import unicode_literals
from django.db import models
import datetime
#import time

class validate(models.Manager):
    def validations(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Title should be al least 5 characters'
        if len(postData['net']) < 3:
            errors['net'] = 'Network should be al least 3 characters'
        if datetime.datetime.now() < datetime.datetime.strptime(postData['date'], "%Y-%m-%d"):
            errors['date'] = 'Date should be in the past'
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors['desc'] = 'Desc should be at least 10 characters'
        return errors


class Tv(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.DateField()
    desc = models.TextField()
    update = models.DateTimeField(auto_now=True)
    objects = validate()