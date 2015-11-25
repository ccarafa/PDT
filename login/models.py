from django.db import models

# Create your models here.

class Signin(models.Model):
	user_id = models.IntegerField(null=True)#null=True for time being
	role = models.CharField(max_length=80)
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=120)

	def __str__(self):
		return self.username