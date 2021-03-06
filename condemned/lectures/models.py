from django.db import models

class BusyMonths(models.Model):
    building = models.CharField(max_length=64, primary_key=True)
    least_busy_month = models.DateField()
    most_busy_month = models.DateField()

    def __unicode__(self):
        least_busy_month = self.least_busy_month.strftime('%b')
        most_busy_month = self.most_busy_month.strftime('%b')
        return "{} {} {}".format(self.building, least_busy_month, most_busy_month)

    class Meta:
        managed = False
        db_table = 'lectures_busy_months'
        ordering = ('building',)

class Room(models.Model):
    building = models.CharField(max_length=64, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)

class Lecture(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    room = models.ForeignKey(Room, null=False)
    date = models.DateTimeField(null=False, blank=False)
