from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''
treview
treview_no, treview_id, tourid, rating, genre 

tuser
tuser_no, tuser_id, tuser_occ, 
tuser_jumin, tuser_gender

travel
tourid, city, town, name, type1, type2, type3, genre

'''
#모델을 다시 바꿔야함...
# 어떻게??




class Travel(models.Model):
    tourid = models.AutoField(primary_key=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    town = models.CharField(max_length=20, blank=True, null=True)
    site = models.CharField(max_length=50, blank=True, null=True)
    genre1 = models.CharField(max_length=20, blank=True, null=True)
    genre2 = models.CharField(max_length=20, blank=True, null=True)
    genre3 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel'


class Treview(models.Model):
    treview_no = models.AutoField(primary_key=True)
    user_no = models.IntegerField(blank=True, null=True)
    placeid = models.IntegerField(db_column='placeid', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'treview'


class Tuser(models.Model):
    user_no = models.AutoField(primary_key=True)
    genre = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    occ = models.IntegerField(blank=True, null=True)
    gen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tuser'



class Usert(models.Model):
    user_no = models.ForeignKey(Tuser, models.DO_NOTHING, db_column='user_no', blank=True, null=True)
    userid = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    etc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usert'


class Tresult(models.Model):
    user_no = models.ForeignKey('Tuser', models.DO_NOTHING, db_column='user_no', blank=True, null=True)
    placeid = models.IntegerField(blank=True, null=True)
    udate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tresult'
