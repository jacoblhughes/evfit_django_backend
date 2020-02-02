from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from habits.models import Habit, HabitMember
from . import models

class CreateHabit(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Habit

class SingleHabit(generic.DetailView):
    model = Habit

class ListHabits(generic.ListView):
    model = Habit


class JoinHabit(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("habits:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        habit = get_object_or_404(Habit,slug=self.kwargs.get("slug"))

        try:
            HabitMember.objects.create(user=self.request.user,habit=habit)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(habit.name)))

        else:
            messages.success(self.request,"You are now a member of the {} habit.".format(habit.name))

        return super().get(request, *args, **kwargs)


class LeaveHabit(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("habits:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:

            membership = models.HabitMember.objects.filter(
                user=self.request.user,
                habit__slug=self.kwargs.get("slug")
            ).get()

        except models.HabitMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this habit because you aren't in it."
            )
        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this habit."
            )
        return super().get(request, *args, **kwargs)
