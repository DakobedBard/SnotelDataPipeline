from django.db import models
from rest_framework.reverse import reverse
from django.conf import settings

class Basins(models.Model):
    basin_id = models.AutoField(primary_key=True)
    basin_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'basins'


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50)
    elevation = models.IntegerField(blank=True, null=True)
    region = models.ForeignKey(Basins, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class SnowpackData(models.Model):
    data_id = models.IntegerField(primary_key=True)
    location_id = models.ForeignKey(to=Locations, on_delete=models.DO_NOTHING)
    date = models.DateField()
    snow_current = models.IntegerField()
    snow_median = models.IntegerField
    snow_pct_median = models.IntegerField
    water_current = models.IntegerField()
    water_avg = models.IntegerField()
    water_pct_avg = models.IntegerField()



