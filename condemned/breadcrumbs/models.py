from django.db import models
from reinvent.mixins import AdjacencyListMixin

class Section(models.Model, AdjacencyListMixin):
    parent = models.ForeignKey('self', null=True)
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return "#{}".format(self.pk)
