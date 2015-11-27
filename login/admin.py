from django.contrib import admin
from .models import Signin
# Register your models here.
class LoginAdmin(admin.ModelAdmin):#this displays more columns in admin panel
    list_display=["__str__","role","username","password"]
    class Meta:
        model = Signin

admin.site.register(Signin, LoginAdmin)
