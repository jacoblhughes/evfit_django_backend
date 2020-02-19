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

class MaxListItem(models.Model):
    max_item_name = models.CharField(max_length = 225, unique=True)
    
    def __str__(self):
        return self.max_item_name

class MaxMultipleRecord(models.Model):
    max_user = models.ForeignKey(User, on_delete=models.CASCADE,)
    created = models.DateField(auto_now_add=True)

    @receiver(post_save,sender=User)
    def create_max_record(sender, instance, created, **kwargs):
        if created:
            MaxMultipleRecord.objects.create(max_user=instance)

    def __str__(self):
        return '{}'.format(
            self.max_user.username
        )

class MaxMultipleMeasurement(models.Model):
    max_record = models.ForeignKey(MaxMultipleRecord, on_delete=models.CASCADE, related_name='maxitemmeasurements')
    max_item = models.ForeignKey(MaxListItem, on_delete = models.CASCADE, related_name= 'max_itementered')
    weight = models.IntegerField()
    unit = models.CharField(max_length=10, default='lb')
    created = models.DateField()

    def __str__(self):
        return '[{}] {} {} taken on {}'.format(
            self.max_record,
            self.max_item,
            self.weight,
            self.created
        )