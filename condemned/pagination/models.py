from django.db import models
from reinvent.managers import PaginationManager

class Person(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=128)
    birth = models.DateField()

    objects = PaginationManager()
