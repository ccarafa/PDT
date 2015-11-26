from django.db import models

# Create your models here.

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
