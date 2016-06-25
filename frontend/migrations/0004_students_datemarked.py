# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20160624_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='datemarked',
            field=models.DateField(default=datetime.datetime(2016, 6, 25, 22, 0, 41, 751582, tzinfo=utc), auto_now_add=True, db_column='DateMarked'),
            preserve_default=False,
        ),
    ]
