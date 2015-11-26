from django.db import models

# Create your models here.

class ActivityModel(models.Model):
    project_id = models.IntegerField(default=0)
    phase_id = models.IntegerField(default=0)
    iteration_id = models.IntegerField(default=0)
    activity_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    # start_time
    # elapsed_time
    # sloc
    # activity_type
    # defects_injected
