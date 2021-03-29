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

class Travel(models.Model):
    tourid = models.IntegerField(db_column='tourId', primary_key=True)  # Field name made lowercase.
    city = models.CharField(max_length=10, blank=True, null=True)
    town = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    genre = models.IntegerField(blank=True, null=True)
    
    #tscore 뭐지...?
    # 이거  tourid , city, town, site, genre

    class Meta:
        managed = False
        db_table = 'travel'


class Treview(models.Model):
    treview_no = models.AutoField(primary_key=True)
    treview_id = models.CharField(max_length=20, blank=True, null=True)
    tourId = models.IntegerField(db_column='tourId', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'treview'

class Tuser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=10, blank=True, null=True)
    user_pwd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tuser'
