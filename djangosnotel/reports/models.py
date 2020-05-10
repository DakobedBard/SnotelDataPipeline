# from django.db import models
#


from django.contrib.postgres.fields import ArrayField
from django.db import models


class Blog(models.Model):
    title = models.CharField( max_length=1000)
    created_at = models.DateTimeField( auto_now_add=True)
    body = models.TextField()
    tags = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    is_published = models.BooleanField( default=False)

    def __str__(self):
        return self.title

class Report(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-id']


