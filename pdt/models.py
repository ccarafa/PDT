from django.db import models

# Create your models here.
class ManagerPhase (models.Model):
	is_open = models.BooleanField(default=False, null = False)
	sloc = models.IntegerField(default=0, null=True)
	est_sloc= models.IntegerField(default=0, null=True)
	hours = models.IntegerField(default=0, null=True)
	defects = models.IntegerField(default=0, null=True)
	phase_name = models.CharField(default="unnamed phase",max_length = 25, null=True)
	project_name = models.CharField(default="unnamed project", max_length = 75, null=False)
	#Riddhi: Make sure the phases an iterations are added automatically one a project is created.
	def __str__(self):
		return self.phase_name

class ManagerIteration (models.Model):
	is_open = models.BooleanField(default=False, null = False)
	sloc = models.IntegerField(default=0, null=True)
	est_sloc= models.IntegerField(default=0, null=True)
	hours = models.IntegerField(default=0, null=True)
	defects = models.IntegerField(default=0, null=True)
	iteration_name = models.CharField(default = "unnamed iteration", max_length = 25, null=True)
	phase_name  = models.CharField(default="unnamed phase", max_length = 75, null=False)
	project_name = models.CharField(default="unnamed project", max_length = 75, null=False)
	#Riddhi: Make sure the phases and iterations are added automatically one a project is created.
	def __str__(self):
		return self.iteration_name
		
class DeveloperPhase (models.Model):
	is_open = models.BooleanField(default=False, null = False)
	sloc = models.IntegerField(null=True)
	hours = models.IntegerField(null=True)
	defects = models.IntegerField(null=True)
	phase_name = models.CharField(default="unnamed phase",max_length = 25, null=True)
	project_name = models.CharField(default="unnamed project", max_length = 75, null=False)
	#Riddhi: Make sure the phases an iterations are added automatically one a project is created.
	def __str__(self):
		return self.phase_name

class DeveloperIteration (models.Model):
	is_open = models.BooleanField(default=False, null = False)
	sloc = models.IntegerField(default=0, null=True)
	hours = models.IntegerField(default=0, null=True)
	defects = models.IntegerField(default=0, null=True)
	iteration_name = models.CharField(default = "unnamed iteration", max_length = 25, null=True)
	phase_name = models.CharField(default="unnamed phase", max_length = 75, null=False)
	project_name = models.CharField(default="unnamed project", max_length = 75, null=False)
	#Riddhi: Make sure the phases and iterations are added automatically one a project is created.
	def __str__(self):
		return self.iteration_name