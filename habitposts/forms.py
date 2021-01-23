from django import forms

from habitposts import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "habit")
        model = models.HabitPost

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["habit"].queryset = (
                models.Habit.objects.filter(
                    pk__in=user.habits.values_list("habit__pk")
                )
            )
