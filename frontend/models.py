# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models


class BookMarked(models.Model):
    idbookmarked = models.AutoField(db_column='idBookMarked', primary_key=True)  # Field name made lowercase.
    idstudent = models.IntegerField(db_column='idStudent', unique=True)  # Field name made lowercase.
    datelastmarked = models.DateField(db_column='DateLastMarked')  # Field name made lowercase.
    
    def studentname(self):
        return Students.objects.get(idstudent=self.idstudent)
        

class Classes(models.Model):
    idclasses = models.AutoField(db_column='idClasses', primary_key=True)
    classname = models.CharField(db_column='ClassName', max_length=30)
    
class Students(models.Model):
    idstudent =  models.AutoField(db_column='idStudents', primary_key=True)
    studentname = models.CharField(db_column='StudentName', max_length=45)
    idclass = models.IntegerField(db_column='idClass')
    
    def classname(self):
        return Classes.objects.get(idclasses=self.idclass)
    