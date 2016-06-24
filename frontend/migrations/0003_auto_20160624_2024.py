# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_bookmarked_classes_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='idclass',
            field=models.IntegerField(db_column='idClass'),
        ),
    ]
