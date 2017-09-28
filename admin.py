from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Nodes, Country, Region, Sity, Site

admin.site.register(Nodes)

# Register your models here.

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Sity)
admin.site.register(Site)