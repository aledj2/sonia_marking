# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_students_datemarked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='datemarked',
            field=models.DateField(auto_now=True, db_column='DateMarked'),
        ),
    ]
