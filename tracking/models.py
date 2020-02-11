from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from habits.models import Habit


# Create your models here.

# def upload_path_documentprofile(instance, filename):
#     return 'efportal/user_programs/{0}/{1}'.format(user.username, filename)


class WeightRecord(models.Model):

    weight_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.weight_user.username


class WeightMeasurement(models.Model):

    weight_record = models.ForeignKey(WeightRecord, on_delete=models.CASCADE, related_name='weightmeasurements')
    weight = models.FloatField()
    unit = models.CharField(max_length=10, default='lb')
    # created = models.DateField(auto_now_add=True)
    created = models.DateField()

    def __str__(self):
        return '[{}] {} {} taken on {}'.format(
            self.weight_record,
            self.weight,
            self.unit,
            self.created
        )

    class Meta:
        ordering = ['-created']

class RMBackSquatRecord(models.Model):

    rmbacksquat_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.rmbacksquat_user.username


class RMBackSquatMeasurement(models.Model):

    rmbacksquat_record = models.ForeignKey(RMBackSquatRecord, on_delete=models.CASCADE, related_name='rmbacksquatmeasurements')
    rmbacksquat = models.FloatField()
    unit = models.CharField(max_length=10, default='lb')
    # created = models.DateField(auto_now_add=True)
    created = models.DateField()

    def __str__(self):
        return '[{}] {} {} taken on {}'.format(
            self.rmbacksquat_record,
            self.rmbacksquat,
            self.unit,
            self.created
        )

    class Meta:
        ordering = ['-created']

class HabitRecord(models.Model):

    habit_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.habit_user.username


class HabitMeasurement(models.Model):

    habit_record = models.ForeignKey(HabitRecord, on_delete=models.CASCADE, related_name='habitmeasurements')
    habit = models.ForeignKey(Habit, on_delete = models.CASCADE, related_name="habitsentered")
    
    REPLY_CHOICES = (("Yes","Yes"),("No","No"))
    reply = models.CharField(max_length = 10, choices=REPLY_CHOICES, default = 1)
    created = models.DateField()

    def __str__(self):
        return '[{}] {} {} taken on {}'.format(
            self.habit_record,
            self.habit,
            self.reply,
            self.created
        )

    class Meta:
        ordering = ['-created']
