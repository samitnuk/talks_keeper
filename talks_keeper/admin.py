from django.contrib import admin

from . import models

admin.site.register(models.Country)
admin.site.register(models.Company)
admin.site.register(models.Talk)
admin.site.register(models.Label)
