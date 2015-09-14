from django.db import models
from reinvent.mixins import AdjacencyListMixin

class Section(models.Model, AdjacencyListMixin):
    parent = models.ForeignKey('self')
    name = models.CharField(max_length=64)
