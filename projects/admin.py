from django.contrib import admin
from .models import Project, ProjectsDeveloper, Phase, Iteration, Activity, DefectsList
# Register your models here.
admin.site.register(Project)
admin.site.register(Iteration)
admin.site.register(Phase)
admin.site.register(ProjectsDeveloper)
admin.site.register(Activity)
admin.site.register(DefectsList)               