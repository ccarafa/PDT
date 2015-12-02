from django.db import models

# Create your models here.
class Project(models.Model):
	project_name = models.CharField(max_length=120, default="-") #project name has to be unique
	is_open = models.BooleanField(default=False)
	estimate_sloc = models.IntegerField(default=0)
	sloc = models.IntegerField(default=0)
	hours = models.IntegerField(default=0)
	manager = models.CharField(max_length=120, default="-")
	estimate_yield = models.IntegerField(default=0)
	is_started=models.BooleanField(default=False)
	def __str__(self):
		return self.project_name

class ProjectsDeveloper(models.Model):
	project_name = models.CharField(max_length=120, default="-")
	developer_name = models.CharField(max_length=120, default="-")
	def __str__(self):
		return self.project_name

class Phase (models.Model):
	is_open = models.BooleanField(default=False)
	phase_name  = models.CharField(max_length=120,default="-")
	project_name = models.CharField(max_length=120,default="-")
	is_started=models.BooleanField(default=False)
	def __str__(self):
		return self.phase_name

class Iteration (models.Model):
	is_open = models.BooleanField(default=False)
	iteration_name = models.CharField(max_length=120,default = "-")
	phase_name  = models.CharField(max_length=200,default="-")
	project_name = models.CharField(max_length=120,default="-")
	is_started=models.BooleanField(default=False)
	twentypercent=models.FloatField(default=0.0)
	def __str__(self):
		return self.iteration_name

class Activity(models.Model):
    project_name = models.CharField(default="unnamed project", max_length=75)
    phase_name = models.CharField(default="unnamed phase", max_length=75)
    iteration_name = models.CharField(default="unnamed iteration", max_length=25)
    activity_type = models.CharField(default='Development', max_length=128)
    username = models.CharField(default='unnamed user', max_length=128)
    start_time = models.CharField(max_length=120, default=0)
    pause_time = models.CharField(max_length=120, default=0)
    duration = models.CharField(max_length=120, default=0)
    sloc = models.FloatField(default=0)
    defects = models.IntegerField(default=0)
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return str(self.project_name+"_"+self.phase_name+"_"+self.iteration_name+"_"+self.username+"_"+self.activity_type)

class Defect(models.Model):
	defect_description = models.CharField(default="-", max_length=500)
	defect_type = models.CharField(default="-", max_length=100)
	project_name = models.CharField(default="-", max_length=75)
	phase_name = models.CharField(default="-", max_length=75)
	iteration_name = models.CharField(default="-", max_length=25)
	username = models.CharField(default='-', max_length=128)
	injected_phase = models.CharField(default='-', max_length=128)
	injected_iteration = models.CharField(default='-', max_length=128)
	defect_id = models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.defect_id)+"_"+self.project_name+"_"+self.injected_phase+"_"+self.injected_iteration+"_"+self.username