# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 20:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_auto_20160705_2010'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookMarked',
        ),
    ]