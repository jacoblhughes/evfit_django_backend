from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

# def upload_path_documentprofile(instance, filename):
#     return 'efportal/user_programs/{0}/{1}'.format(user.username, filename)


class EFUser(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique = True)
    birth_date = models.DateField(null=True, blank = True)
    # profile_image = models.ImageField(upload_to = 'efportal/profile_image/',blank = True, default="efportal/profile_image/default.png")
    habit = models.ForeignKey('habits.Habit', related_name='profile', null=True, on_delete=models.CASCADE)

    @receiver(post_save,sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return "{} Profile".format(self.user.username)


# class DocumentProfile(models.Model):

#     user = models.OneToOneField(User, on_delete=models.CASCADE, unique = True)
#     program = models.FileField(upload_to = 'efportal/user_programs/', blank = True, default = "efportal/user_programs/welcome.xlsx")

#     @receiver(post_save, sender = User)
#     def create_user_program(sender, instance, created, **kwargs):
#         if created:
#             DocumentProfile.objects.create(user=instance)
    
#     def __str__(self):
#         return "{} Document Profile".format(self.user.username)