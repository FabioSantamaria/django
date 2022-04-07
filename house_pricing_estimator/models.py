from django.db import models

# Create your models here.

class Houses(models.Model):
	floor_number = models.IntegerField()
	year_construction = models.IntegerField()
	square_meters = models.FloatField()
	rooms_number = models.IntegerField()
	baths_number = models.IntegerField()