from django.contrib import admin
from . import models

# Register your models here.

class WorkoutTemplateAdmin(admin.ModelAdmin):
    ordering = ['title']

admin.site.register(models.WorkoutTemplate)