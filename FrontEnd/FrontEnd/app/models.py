from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Prediction(models.Model):
	algorithm_name = models.CharField(max_length=100)
	value = models.IntegerField()
	last_entered = models.DateTimeField()