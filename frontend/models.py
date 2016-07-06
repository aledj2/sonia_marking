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


################################################################################
# class BookMarked(models.Model):
#     idbookmarked = models.AutoField(db_column='idBookMarked', primary_key=True)  # Field name made lowercase.
#     idstudent = models.IntegerField(db_column='idStudent', unique=True)  # Field name made lowercase.
#     datelastmarked = models.DateField(db_column='DateLastMarked')  # Field name made lowercase.
#     
#     def studentname(self):
#         return Students.objects.get(idstudent=self.idstudent)
#     
#     class Meta:
#         verbose_name_plural="Books"
################################################################################

class Classes(models.Model):
    idclasses = models.AutoField(db_column='idClasses', primary_key=True)
    classname = models.CharField(db_column='ClassName', max_length=30)
    class Meta:
        verbose_name_plural="Classes"
        
class Students(models.Model):
    idstudent =  models.AutoField(db_column='idStudents', primary_key=True)
    studentname = models.CharField(db_column='StudentName', max_length=45)
    idclass = models.IntegerField(db_column='idClass')
    datemarked = models.DateField(db_column='DateMarked',auto_now=True, auto_now_add=False)
    progress1_date=models.DateField(db_column='Progress1_date',auto_now=False, auto_now_add=False, null = True)
    progress2_date=models.DateField(db_column='Progress2_date',auto_now=False, auto_now_add=False, null = True)
    progress3_date=models.DateField(db_column='Progress3_date',auto_now=False, auto_now_add=False,null = True)
    progress4_date = models.DateField(db_column='Progress4_date',auto_now=False, auto_now_add=False,null = True)
    progress5_date=models.DateField(db_column='Progress5_date',auto_now=False, auto_now_add=False,null = True)
    progress6_date=models.DateField(db_column='Progress6_date',auto_now=False, auto_now_add=False,null = True)
    progress7_date=models.DateField(db_column='Progress7_date',auto_now=False, auto_now_add=False,null = True)
    datemarkedprogress=models.IntegerField(db_column='DateMarkedProgress')
    progress1=models.IntegerField(db_column='progress1')
    progress2=models.IntegerField(db_column='progress2')
    progress3=models.IntegerField(db_column='progress3')
    progress4=models.IntegerField(db_column='progress4')
    progress5=models.IntegerField(db_column='progress5')
    progress6=models.IntegerField(db_column='progress6')
    progress7=models.IntegerField(db_column='progress7')
    
    def classname(self):
        return Classes.objects.get(idclasses=self.idclass)
    
    def progress1_text(self):
        progress_name= Progress.objects.get(idprogress=self.progress1)
        return progress_name
    
    def progress2_text(self):
        progress_name= Progress.objects.get(idprogress=self.progress2)
        return progress_name
    
    def progress3_text(self):
        progress_name= Progress.objects.get(idprogress=self.progress3)
        return progress_name
    
    def progress4_text(self):
        progress_name= Progress.objects.get(idprogress=self.progress4)
        return progress_name
    
    def progress5_text(self):
        progress_name= Progress.objects.get(idprogress=self.progress5)
        return progress_name
    
    def progress6_text(self):
        progress_name= Progress.objects.get(idprogress=self.progress6)
        return progress_name
    
    def progress7_text(self):
        progress_name= Progress.objects.get(idprogress=self.progress7)
        return progress_name
    
    def datemarkedprogress_text(self):
        progress_name= Progress.objects.get(idprogress=self.datemarkedprogress)
        return progress_name
    
    class Meta:
        verbose_name_plural="Students"
    
class Progress(models.Model):
    idprogress =  models.AutoField(db_column='idProgress', primary_key=True)
    progress_text = models.CharField(db_column='ProgressName', max_length=45)
    class Meta:
        verbose_name_plural="Progress"