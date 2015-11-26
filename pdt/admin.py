from django.contrib import admin
from .models import ManagerIteration
from .models import ManagerPhase
from .models import DeveloperIteration
from .models import DeveloperPhase
# Register your models here.

admin.site.register(ManagerPhase)
admin.site.register(ManagerIteration)
admin.site.register(DeveloperPhase)
admin.site.register(DeveloperIteration)