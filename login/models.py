from django.db import models

# Create your models here.

class User(models.Model):
	user_id = models.IntegerField()
	role = models.CharField(max_length=80)
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=120)

	def __str__(self):
		return self.username
