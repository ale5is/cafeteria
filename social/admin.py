from django.contrib import admin
from .models import link

class linkAdmin(admin.ModelAdmin):
    pass

admin.site.register(link, linkAdmin)
