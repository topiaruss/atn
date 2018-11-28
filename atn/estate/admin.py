from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Zone, Site

admin.site.register(Zone)
admin.site.register(Site)