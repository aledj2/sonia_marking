# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookMarked',
            fields=[
                ('idbookmarked', models.AutoField(serialize=False, primary_key=True, db_column='idBookMarked')),
                ('idstudent', models.IntegerField(unique=True, db_column='idStudent')),
                ('datelastmarked', models.DateField(db_column='DateLastMarked')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('idclasses', models.AutoField(serialize=False, primary_key=True, db_column='idClasses')),
                ('classname', models.CharField(max_length=30, db_column='ClassName')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('idstudent', models.AutoField(serialize=False, primary_key=True, db_column='idStudents')),
                ('studentname', models.CharField(max_length=45, db_column='StudentName')),
                ('idclass', models.IntegerField(max_length=5, db_column='idClass')),
            ],
        ),
    ]
