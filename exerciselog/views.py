from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy


from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from exerciselog.models import ExerciseRecord, ExerciseInformation
from . import models
from . import forms
# Create your views here.

class ListExercise(generic.ListView):
    model = ExerciseInformation

class CreateExercise(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('exercise','created',)
    success_url = reverse_lazy('exerciselog:exercise_list')

    model = models.ExerciseInformation

    # form_class = forms.ExerciseInformationForm


    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)

    def get_form(self):
        '''add date picker in forms'''
        from django.forms.widgets import SelectDateWidget
        form = super(CreateExercise, self).get_form()
        form.fields['created'].widget = SelectDateWidget()
        return form

    def form_valid(self, form):
        form.instance.exercise_record = ExerciseRecord.objects.get(exercise_user=self.request.user)
        return super().form_valid(form)