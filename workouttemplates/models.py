from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django import forms

# Create your models here.
class WorkoutTemplate(models.Model):
    category = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    template = models.TextField(max_length=1000, null=True, blank=True)
    notes = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(
            self.title, self.category
        )