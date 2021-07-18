from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class DoctorFormModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    password=models.CharField(db_column='password',max_length=10)
    DoctorID=models.CharField(db_column='doctorID',max_length=9)
    doctorName=models.TextField(db_column='doctorName')
    class Meta:
        managed = True
        db_table = 'doctormodel'

class PatientsymptomesModel(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taz = models.CharField(db_column='taz',max_length=9)
    name = models.TextField(db_column='name')
    smoke = models.TextField(db_column='smoke')
    age = models.TextField(db_column='age')
    Origine = models.TextField(db_column='Origine')
    message = models.TextField(db_column='message')
    alk_phos = models.FloatField(db_column='Alk_Phos')  # Field name made lowercase.
    hdl = models.FloatField(db_column='HDL')  # Field name made lowercase.
    iron = models.FloatField(db_column='Iron')  # Field name made lowercase.
    creat = models.FloatField(db_column='Creat')  # Field name made lowercase.
    hb = models.FloatField(db_column='Hb')  # Field name made lowercase.
    urea = models.FloatField(db_column='Urea')  # Field name made lowercase.
    hct = models.FloatField(db_column='HCT')  # Field name made lowercase.
    rbc = models.FloatField(db_column='RBC')  # Field name made lowercase.
    lymph = models.FloatField(db_column='Lymph')  # Field name made lowercase.
    neut = models.FloatField(db_column='Neut')  # Field name made lowercase.
    wbc = models.FloatField(db_column='WBC')  # Field name made lowercase.
    testresult = models.TextField(db_column='testResult')
    gender = models.TextField(db_column='gender')
    DoctorDescript = models.TextField(db_column='DoctorDescript')
    Treatement=models.TextField(db_column='Treatement')
  
    class Meta:
        managed = True
        db_table = 'patientsymptomes'
