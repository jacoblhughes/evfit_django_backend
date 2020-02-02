from django.contrib import admin
from . import models
# Register your models here.

class HabitMemberInline(admin.TabularInline):
    habit = models.HabitMember

admin.site.register(models.Habit)

admin.site.register(models.HabitMember)

