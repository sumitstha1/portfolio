from django.contrib import admin
from .models import AppUser

# Register your models here.
admin.site.site_header = "Portfolio"
admin.site.site_title = "Portfolio"


admin.site.register(AppUser)