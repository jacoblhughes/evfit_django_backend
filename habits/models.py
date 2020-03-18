from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# Create your models here.

class Habit(models.Model):
    name = models.TextField(max_length=255, unique=True, blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="HabitMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("habits:single", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ["name"]

class HabitMember(models.Model):
    habit = models.ForeignKey(Habit, related_name="memberships",on_delete = models.CASCADE)
    user = models.ForeignKey(User,related_name='user_habits', on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username + ' ' + str(self.habit)
        

    class Meta:
        unique_together = ("habit", "user")