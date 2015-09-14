# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from reinvent.migrations import RunSQLFile


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        RunSQLFile(__file__),
        migrations.CreateModel(
            name='BusyMonths',
            fields=[
                ('building', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('least_busy_month', models.DateField()),
                ('most_busy_month', models.DateField()),
            ],
            options={
                'ordering': ('building',),
                'db_table': 'university_busy_months',
                'managed': False,
            },
        ),
    ]
