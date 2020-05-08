# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Basins(models.Model):
    basin_id = models.AutoField(primary_key=True)
    basin_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'basins'


class BasinsAggregate(models.Model):
    region = models.IntegerField()
    pct_median = models.IntegerField(blank=True, null=True)
    pct_avg = models.IntegerField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'basins_aggregate'


class DateTable(models.Model):
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'date_table'


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50)
    elevation = models.IntegerField(blank=True, null=True)
    region = models.ForeignKey(Basins, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Snowpack(models.Model):
    location_id = models.IntegerField()
    date = models.DateField()
    snow_current = models.IntegerField()
    snow_median = models.IntegerField()
    snow_pct_median = models.IntegerField()
    water_current = models.IntegerField()
    water_avg = models.IntegerField()
    water_pct_avg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'snowpack'
