from django.contrib import admin
from . import models

# Register your models here.

class ExpoRecordAdmin(admin.ModelAdmin):
    ordering = ['expo_user__username']

admin.site.register(models.ExpoRecord)