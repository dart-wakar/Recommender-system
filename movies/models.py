from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=100,blank=True)
    details = models.CharField(max_length=250,blank=True)

    class Meta:
        ordering = ('id',)
