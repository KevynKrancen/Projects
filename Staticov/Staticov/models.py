from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class worker_register(models.Model):
    ID = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userid', max_length=9)  # Field name made lowercase.
    name= models.TextField(db_column='name')
    password = models.CharField(db_column='password',max_length=10)

    class Meta:
        managed = True
        db_table = 'worker-register'

class AdminModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    taz=models.CharField(db_column='taz',max_length=9)
    password=models.TextField(db_column='Password')
    class Meta:
        managed = False
        db_table = 'admin'

class WorkersModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    taz=models.CharField(db_column='taz',max_length=9)
    password=models.TextField(db_column='password')
    Type=models.TextField(db_column='type')
    class Meta:
        managed = True
        db_table = 'workers'

class CivilianModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    taz=models.CharField(db_column='taz',max_length=9)
    age=models.IntegerField(db_column='age')
    place=models.TextField(db_column='place')
    date=models.DateField(db_column='date')
    religion=models.TextField(db_column='religion')
    class Meta:
        managed = False
        db_table = 'formcivilian'

class IndexFormModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    taz=models.CharField(db_column='taz',max_length=9)
    telephone=models.CharField(db_column='telephone',max_length=11)
    symptomes=models.TextField(db_column='symptomes')
    age=models.CharField(db_column='age',max_length=3)
    workerid=models.IntegerField(db_column='workerid')
    class Meta:
        managed = False
        db_table = 'indexform'
   

class RegisterFormModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    taz=models.CharField(db_column='taz',max_length=9)
    password=models.TextField(db_column='password')
    Type=models.TextField(db_column='type')
    civiliantype=models.TextField(db_column='civiliantype')
    
    class Meta:
        managed = True
        db_table = 'registerform'


class SymptomesFormModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    head=models.TextField(db_column='head')
    hot=models.TextField(db_column='hot')
    smell=models.TextField(db_column='smell')
    hurts=models.TextField(db_column='hurts')
    class Meta:
        managed = False
        db_table = 'symptomesform'


class Popup(models.Model):
    mid = models.IntegerField(db_column='MID', primary_key=True)  # Field name made lowercase.
    popupmsg = models.TextField(db_column='popupmsg')

    class Meta:
        managed = True
        db_table = 'popup'

class emploiedutemp(models.Model):
    ID = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    startdate = models.TextField(db_column='startdate')
    enddate = models.TextField(db_column='enddate')
    workerid = models.CharField(db_column='workerid',max_length=9)
    confirmation = models.TextField(db_column='confirmation')

    class Meta:
        managed = False
        db_table = 'emploiedutemp'