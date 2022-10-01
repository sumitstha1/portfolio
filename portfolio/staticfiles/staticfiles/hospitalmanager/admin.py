from django.contrib import admin
from .models import Appointment
# Register your models here.

admin.site.site_title = "Hospital Manager"
admin.site.site_header = "Hospital Manager"
admin.site.index_title = "Hospital Manager"

admin.site.register(Appointment)