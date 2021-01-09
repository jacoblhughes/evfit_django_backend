from django import forms

from . import models

class DateInput(forms.DateInput):
    input_type = 'date'

class MaxMultipleMeasurementForm(forms.ModelForm):

    class Meta:
        model = models.MaxMultipleMeasurement
        fields = ("max_item", "weight","created")
        widgets = {
            'created': DateInput(format = '%Y/%m/%d')
        }


class WeightMeasurementForm(forms.ModelForm):

    class Meta:
        model = models.WeightMeasurement
        fields = ("weight","created")
        widgets = {
            'created': DateInput(format = '%Y/%m/%d')
        }

# class HabitMeasurementForm(forms.ModelForm):

#     class Meta:
#         model = models.HabitMeasurement
#         fields = ("habit","reply","created")
#         widgets = {
#             'created': DateInput(format = '%Y/%m/%d')
#         }