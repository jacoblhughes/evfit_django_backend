from django.contrib import admin
from . import models

# Register your models here.

class WeightRecordAdmin(admin.ModelAdmin):
    ordering = ['weight_user__username']


class WeightMeasurementAdmin(admin.ModelAdmin):
    ordering = ['-created']


admin.site.register(models.WeightRecord, WeightRecordAdmin)
admin.site.register(models.WeightMeasurement, WeightMeasurementAdmin)


class HabitRecordAdmin(admin.ModelAdmin):
    ordering = ['habit_user__username']


class HabitMeasurementAdmin(admin.ModelAdmin):
    ordering = ['-created']


admin.site.register(models.HabitRecord, HabitRecordAdmin)
admin.site.register(models.HabitMeasurement, HabitMeasurementAdmin)



admin.site.register(models.MaxListItem)
admin.site.register(models.MaxMultipleRecord)
admin.site.register(models.MaxMultipleMeasurement)

