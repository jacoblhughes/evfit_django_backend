from django.shortcuts import render

# Create your views here.
from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.list import ListView
from django.views import View
from .models import WeightMeasurement, WeightRecord, RMBackSquatMeasurement, RMBackSquatRecord, HabitRecord, HabitMeasurement
from habits.models import Habit

class TrackingHome(TemplateView):
    template_name = 'tracking/tracking_base.html'

class WeightData(View):
    def get(self, request):
        weight_data = {}
        unit = request.GET.get('unit')
        for record in WeightRecord.objects.all():
            name = record.weight_user.username
            name = name.strip()
            weight_data[name] = {
                # 'colour': _get_preferred_colour(record),
                'weightmeasurements': []
            }
            for weightmeasurement in record.weightmeasurements.all():
                weight_data[name]['weightmeasurements'].append(
                    {'created': weightmeasurement.created, 'weight': weightmeasurement.weight, 'unit': weightmeasurement.unit}
                )
        return JsonResponse(weight_data)

    # return HttpResponse(status=400, reason='Only GET requests are allowed')


class WeightTableView(LoginRequiredMixin, ListView):

    model = WeightMeasurement
    template_name = 'tracking/weight_table.html'

    def get_queryset(self):
        return WeightMeasurement.objects.filter(
            weight_record=WeightRecord.objects.get(weight_user=self.request.user))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page'] = 'weight_table'
        unit = 'lb'

        measurements = []

        for measurement in data['object_list']:
            measurements.append({
                'weight': measurement.weight,
                'created': measurement.created if measurement.created != date.today() else 'Today',
                'unit': measurement.unit,
            })

        data['object_list'] = measurements
        return data


class AddWeightMeasurementView(LoginRequiredMixin, CreateView):

    model = WeightMeasurement
    fields = ['weight', 'unit']
    template_name = 'tracking/add.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page'] = 'add'
        data['show_form'] = True

        latest = WeightMeasurement.objects.filter(
            weight_record=WeightRecord.objects.get(weight_user=self.request.user)
        )

        if latest and latest[0].created == date.today():
            data['show_form'] = False

        return data

    def form_valid(self, form):
        form.instance.weight_record = WeightRecord.objects.get(weight_user=self.request.user)
        return super().form_valid(form)

class RMBackSquatData(View):
    def get(self, request):
        rmbacksquat_data = {}
        unit = request.GET.get('unit')
        for record in RMBackSquatRecord.objects.all():
            name = record.rmbacksquat_user.username
            name = name.strip()
            rmbacksquat_data[name] = {
                # 'colour': _get_preferred_colour(record),
                'rmbacksquatmeasurements': []
            }
            for rmbacksquatmeasurement in record.rmbacksquatmeasurements.all():
                rmbacksquat_data[name]['rmbacksquatmeasurements'].append(
                    {'created': rmbacksquatmeasurement.created, 'rmbacksquat': rmbacksquatmeasurement.rmbacksquat, 'unit': rmbacksquatmeasurement.unit}
                )
        return JsonResponse(rmbacksquat_data)

    # return HttpResponse(status=400, reason='Only GET requests are allowed')


class RMBackSquatTableView(LoginRequiredMixin, ListView):

    model = RMBackSquatMeasurement
    template_name = 'tracking/rmbacksquat_table.html'

    def get_queryset(self):
        return RMBackSquatMeasurement.objects.filter(
            rmbacksquat_record=RMBackSquatRecord.objects.get(rmbacksquat_user=self.request.user))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page'] = 'rmbacksquat_table'
        unit = 'lb'

        measurements = []

        for measurement in data['object_list']:
            measurements.append({
                'rmbacksquat': measurement.rmbacksquat,
                'created': measurement.created if measurement.created != date.today() else 'Today',
                'unit': measurement.unit,
            })

        data['object_list'] = measurements
        return data

class HabitData(View):
    def get(self, request):
        habit_data = {}
        habit_data['count'] = Habit.objects.all().count()
        habit_data['habits'] = {}
        for habit in Habit.objects.all():
            habit_data['habits'].update({habit.pk:habit.name})
        reply = request.GET.get('reply')
        for record in HabitRecord.objects.all():
            name = record.habit_user.username
            name = name.strip()
            habit_data[name] = {
                # 'colour': _get_preferred_colour(record),
                'habitmeasurements': []
            }
            for habitmeasurement in record.habitmeasurements.all():
                habit_data[name]['habitmeasurements'].append(
                    {'created': habitmeasurement.created, 'habit': habitmeasurement.habit.pk, 'reply': habitmeasurement.reply}
                )
        return JsonResponse(habit_data)

    # return HttpResponse(status=400, reason='Only GET requests are allowed')


class HabitTableView(LoginRequiredMixin, ListView):

    model = HabitMeasurement
    template_name = 'tracking/habit_table.html'

    def get_queryset(self):
        return HabitMeasurement.objects.filter(
            habit_record=HabitRecord.objects.get(habit_user=self.request.user))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page'] = 'habit_table'
        

        measurements = []

        for measurement in data['object_list']:
            measurements.append({
                'habit': measurement.habit,
                'created': measurement.created if measurement.created != date.today() else 'Today',
                'reply': measurement.reply,
            })

        data['object_list'] = measurements
        return data