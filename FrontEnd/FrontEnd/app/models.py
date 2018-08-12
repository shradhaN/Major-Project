from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Parameters(models.Model):
	algorithm_name = models.CharField(max_length=100)
	precision = models.FloatField()
	accuracy = models.FloatField()
	hit = models.FloatField()
	tnr = models.FloatField()
	miss = models.FloatField()
	fallout = models.FloatField()
	f1score = models.FloatField()
	tp= models.FloatField(null = True)
	fp= models.FloatField(null = True)
	tn= models.FloatField(null = True)
	fn= models.FloatField(null = True)

class data_set(models.Model):
	date = models.CharField(max_length = 50)
	time = models.CharField(max_length = 50)
	action = models.CharField(max_length = 120)
	protocol = models.CharField(max_length = 100)
	src_ip = models.FloatField()
	dst_ip=models.FloatField()
	src_port = models.FloatField()
	dst_port = models.FloatField()
	path = models.FloatField()

class classified_data(models.Model):
	category =  models.FloatField()
	data_set = models.ForeignKey(data_set, on_delete = models.CASCADE)

class data_set_normalized(models.Model):
 	action_normal = models.FloatField()
 	protocol_normal = models.FloatField()
 	src_ip_normal=models.FloatField()
 	dst_ip_normal = models.FloatField()
 	path_normal = models.FloatField()
 	data_set = models.OneToOneField(data_set, on_delete=models.CASCADE)
 	
class actual_value(models.Model):
	positive= models.FloatField(null = True)
	negative= models.FloatField(null = True)


