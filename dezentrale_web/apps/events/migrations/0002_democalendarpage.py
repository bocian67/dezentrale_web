# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-08 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joyous', '0003_extrainfopage_extra_title'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoCalendarPage',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name': 'Calendar Demo',
                'proxy': True,
            },
            bases=('joyous.calendarpage',),
        ),
    ]
