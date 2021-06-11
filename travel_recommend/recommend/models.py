from django.db import models
from django.contrib.auth.models import User

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
    user_no = models.ForeignKey('Tuser', models.DO_NOTHING, db_column='user_no', blank=True, null=True)
    placeid = models.ForeignKey(Travel, models.DO_NOTHING, db_column='placeid', blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    treview_no = models.AutoField(primary_key=True)
    udate = models.DateTimeField(blank=True, null=True)

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
