from django.conf import settings
from django.urls import reverse
from django.db import models


from habits.models import Habit

from django.contrib.auth import get_user_model
User = get_user_model()


class HabitPost(models.Model):
    user = models.ForeignKey(User, related_name="habituser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    habit = models.ForeignKey(Habit, related_name="habitposts", on_delete=models.CASCADE)
    # username = models.CharField(max_length=100)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        # self.username = self.user.username
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "habitposts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message",'created_at']

