from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Prediction(models.Model):
	algorithm_name = models.CharField(max_length=100)
	value = models.IntegerField()
	last_entered = models.DateTimeField()

class data_set(models.Model):
	date_time = models.DateTimeField()
	action = models.CharField(max_length = 100)
	protocol = models.CharField(max_length = 100)
	src_ip = models.FloatField()
	dst_ip=models.FloatField()
	src_port = models.FloatField()
	dst_port = models.FloatField()
	path = models.FloatField()

class classified_data(models.Model):
	category =  models.FloatField()
	data_set = models.OneToOneField(data_set, on_delete = models.CASCADE)

