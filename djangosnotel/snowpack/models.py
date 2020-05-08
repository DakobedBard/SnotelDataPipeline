from django.db import models
from rest_framework.reverse import reverse
from django.conf import settings


class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    location_name = models.CharField(max_length=50, default="document")
    name = models.CharField(max_length=30, default="document.txt")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default =1 )
    def __str__(self):
        return "The dioc is " + self.name + " and the user is " + self.user

class SnowpackData(models.Model):
    data_id = models.IntegerField(primary_key=True)
    location_id = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    date = models.DateField()
    snow_current = models.IntegerField()
    snow_median = models.IntegerField
    snow_pct_median = models.IntegerField
    water_current = models.IntegerField()
    water_avg = models.IntegerField()
    water_pct_avg = models.IntegerField()
