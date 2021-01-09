from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from habits.models import Habit
from django.utils.text import slugify


# Create your models here.

# def upload_path_documentprofile(instance, filename):
#     return 'efportal/user_programs/{0}/{1}'.format(user.username, filename)


class WeightRecord(models.Model):

    weight_user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    created = models.DateField(auto_now_add=True)

    @receiver(post_save,sender=User)
    def create_weight_record(sender, instance, created, **kwargs):
        if created:
            WeightRecord.objects.create(weight_user=instance)

    def __str__(self):
        return self.weight_user.username


class WeightMeasurement(models.Model):

    weight_record = models.ForeignKey(WeightRecord, on_delete=models.CASCADE, related_name='weightmeasurements')
    weight = models.FloatField()
    unit = models.CharField(max_length=10, default='lb')
    # created = models.DateField(auto_now_add=True)
    created = models.DateTimeField()
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        created_slug = str(self.weight_record) +'-'+ str(self.weight) +'-'+ str(self.created)
        self.slug = slugify(created_slug)
        super().save(*args, **kwargs)

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

    habit_user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    created = models.DateField(auto_now_add=True)

    @receiver(post_save,sender=User)
    def create_habit_record(sender, instance, created, **kwargs):
        if created:
            HabitRecord.objects.create(habit_user=instance)

    def __str__(self):
        return self.habit_user.username


class HabitMeasurement(models.Model):

    habit_record = models.ForeignKey(HabitRecord, on_delete=models.CASCADE, related_name='habitmeasurements')
    habit = models.ForeignKey(Habit, on_delete = models.CASCADE, related_name="habitsentered")
    
    REPLY_CHOICES = (("Yes","Yes"),("No","No"))
    reply = models.CharField(max_length = 10, choices=REPLY_CHOICES, default = 1)
    created = models.DateTimeField()
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        created_slug = str(self.habit_record) +'-'+ str(self.habit) +'-'+ str(self.created)
        self.slug = slugify(created_slug)
        super().save(*args, **kwargs)

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
    max_user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
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
    created = models.DateTimeField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        created_slug = str(self.max_record) +''+ str(self.max_item)+''+ str(self.weight) +''+ str(self.created)
        self.slug = slugify(created_slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return '[{}] {} {} taken on {}'.format(
            self.max_record,
            self.max_item,
            self.weight,
            self.created
        )