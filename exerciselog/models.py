from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django import forms



# Create your models here.
class ExerciseRecord(models.Model):

    exercise_user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    created = models.DateField(auto_now_add=True)

    @receiver(post_save,sender=User)
    def create_exercise_record(sender, instance, created, **kwargs):
        if created:
            ExerciseRecord.objects.create(exercise_user=instance)

    def __str__(self):
        return self.exercise_user.username


class ExerciseInformation(models.Model):

    exercise_record = models.ForeignKey(ExerciseRecord, on_delete=models.CASCADE, related_name='exerciseformation')
    exercise = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return '[{}] taken on {}'.format(
            self.exercise_record,
            self.created
        )

    class Meta:
        ordering = ['-created']