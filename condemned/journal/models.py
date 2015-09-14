from django.db import models
from django.contrib.postgres.fields import JSONField

class Event(models.Model):
    datetime = models.DateTimeField()
    message = JSONField()
