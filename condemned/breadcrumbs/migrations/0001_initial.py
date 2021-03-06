# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-10-12 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import reinvent.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='breadcrumbs.Section', null=True)),
            ],
            bases=(models.Model, reinvent.mixins.AdjacencyListMixin),
        ),
    ]
