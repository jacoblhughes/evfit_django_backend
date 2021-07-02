from django import forms

from . import models

class DateInput(forms.DateInput):
    input_type = 'date'

class ExerciseInformationForm(forms.ModelForm):

    class Meta:
        model = models.ExerciseInformation
        fields = ("exercise","created")
        labels = {"",""}
        widgets = {
            'created': DateInput(format = '%Y/%m/%d')
        }