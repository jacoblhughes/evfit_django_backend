from django.contrib import admin
from . import models

# Register your models here.

class WeightRecordAdmin(admin.ModelAdmin):
    ordering = ['weight_user__username']


class WeightMeasurementAdmin(admin.ModelAdmin):
    ordering = ['-created']


admin.site.register(models.WeightRecord, WeightRecordAdmin)
admin.site.register(models.WeightMeasurement, WeightMeasurementAdmin)

class RMBackSquatRecordAdmin(admin.ModelAdmin):
    ordering = ['rmbacksquat_user__username']


class RMBackSquatMeasurementAdmin(admin.ModelAdmin):
    ordering = ['-created']


admin.site.register(models.RMBackSquatRecord, RMBackSquatRecordAdmin)
admin.site.register(models.RMBackSquatMeasurement, RMBackSquatMeasurementAdmin)

class HabitRecordAdmin(admin.ModelAdmin):
    ordering = ['habit_user__username']


class HabitMeasurementAdmin(admin.ModelAdmin):
    ordering = ['-created']


admin.site.register(models.HabitRecord, HabitRecordAdmin)
admin.site.register(models.HabitMeasurement, HabitMeasurementAdmin)
