# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_scoreevent_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.FileField(blank=True, upload_to='taskdata/', verbose_name='File'),
        ),
    ]
