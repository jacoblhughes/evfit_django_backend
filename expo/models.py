from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django import forms

# Create your models here.
class ExpoRecord(models.Model):
    expo_user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    expoToken = models.CharField(max_length=250, null=True, blank=True)
    expoAccepted = models.BooleanField(null=True, default = False)
    
    @receiver(post_save,sender=User)
    def create_expo_record(sender, instance, created, **kwargs):
        if created:
            ExpoRecord.objects.create(expo_user=instance)

    def __str__(self):
        return '{} Expo Profile'.format(
            self.expo_user.username
        )