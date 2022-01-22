from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class admin(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    password=models.CharField(db_column='password',max_length=10)
    class Meta:
        managed = True
        db_table = ' admin'

class barmaid(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    password=models.CharField(db_column='password',max_length=10)
    class Meta:
        managed = True
        db_table = ' barmaid'

class vipclient(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    age=models.IntegerField(db_column='age')
    CN=models.IntegerField(db_column='CN')
    password=models.CharField(db_column='password',max_length=10)
    confirmation=models.IntegerField(db_column='confirmation')
    phone=models.TextField(db_column='phone')
    class Meta:
        managed = True
        db_table = ' vipclient'

class client(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    confirmation=models.IntegerField(db_column='confirmation')
    class Meta:
        managed = True
        db_table = ' client'

class outsidetable(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    occupied=models.IntegerField(db_column='occupied')
    places=models.IntegerField(db_column='places')
    class Meta:
        managed = True
        db_table = ' outsidetable'

class insidetable(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    occupied=models.TextField(db_column='occupied')
    places=models.IntegerField(db_column='places')
    type=models.TextField(db_column='type')
    class Meta:
        managed = True
        db_table = ' insidetable'

class Menu(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    type=models.TextField(db_column='type')
    price=models.IntegerField(db_column='price')
    popularity=models.IntegerField(db_column='popularity')
    alcool=models.BooleanField(db_column='alcool')
    description=models.TextField(db_column='description')
    avaibility=models.BooleanField(db_column='avaibility')
    photo=models.TextField(db_column='photo')
    class Meta:
        managed = True
        db_table = 'menu'
        ordering = ['price']

class lunch(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    type=models.TextField(db_column='type')
    price=models.IntegerField(db_column='price')
    popularity=models.IntegerField(db_column='popularity')
    alcool=models.IntegerField(db_column='alcool')
    description=models.TextField(db_column='description')
    image=models.IntegerField(db_column='image')
    avaibility=models.IntegerField(db_column='avaibility')
    class Meta:
        managed = True
        db_table = ' lunch'

class party(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    type=models.TextField(db_column='type')
    price=models.IntegerField(db_column='price')
    popularity=models.IntegerField(db_column='popularity')
    alcool=models.IntegerField(db_column='alcool')
    description=models.TextField(db_column='description')
    image=models.IntegerField(db_column='image')
    avaibility=models.IntegerField(db_column='avaibility')
    class Meta:
        managed = True
        db_table = ' party'

class order(models.Model):
    OID=models.IntegerField(db_column='OID',primary_key=True)
    MID=models.TextField(db_column='MID')
    TABLE=models.IntegerField(db_column='TABLE')
    price=models.IntegerField(db_column='price')
    vip=models.TextField(db_column='vip')
    class Meta:
        managed = True
        db_table = 'order'
        