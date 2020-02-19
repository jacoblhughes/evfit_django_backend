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
from .models import WeightMeasurement, WeightRecord, HabitRecord, HabitMeasurement, MaxListItem, MaxMultipleRecord, MaxMultipleMeasurement
from habits.models import Habit
from tracking.models import HabitMeasurement

from braces.views import SelectRelatedMixin

from plotly.offline import plot
from plotly.graph_objs import Scatter


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


class AddWeightView(LoginRequiredMixin, CreateView):
    model = WeightMeasurement
    fields = ['weight', 'created']
    template_name = 'tracking/weight_form.html'
    success_url = reverse_lazy('tracking:tracking')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page'] = 'weight_add'
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

        # x_data = [0,1,2,3]
        # y_data = [x**2 for x in x_data]
        # plotly_div = plot([Scatter(x=x_data, y=y_data,
        #                 mode='lines', name='test',
        #                 opacity=0.8, marker_color='green')],
        #        output_type='div')
        # data['plotly'] = plotly_div

        return data

class AddHabitView(LoginRequiredMixin, CreateView):
    fields = ['habit','reply','created']
    template_name = 'tracking/habit_form.html'
    success_url = reverse_lazy('tracking:tracking')

    model = HabitMeasurement

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page'] = 'habit_form'
        data['show_form'] = True

        latest = HabitMeasurement.objects.filter(
            habit_record=HabitRecord.objects.get(habit_user=self.request.user)
        )

        if latest and latest[0].created == date.today():
            data['show_form'] = False

        return data

    def form_valid(self, form):
        form.instance.habit_record = HabitRecord.objects.get(habit_user=self.request.user)
        return super().form_valid(form)


class MaxData(View):
    def get(self, request):
        maxitem_data = {}
        maxitem_data['count'] = MaxListItem.objects.all().count()
        maxitem_data['maxitems'] = {}
        for maxitem in MaxListItem.objects.all():
            maxitem_data['maxitems'].update({maxitem.pk:maxitem.max_item_name})
        weight = request.GET.get('weight')
        for record in MaxMultipleRecord.objects.all():
            name = record.max_user.username
            name = name.strip()
            maxitem_data[name] = {}
            maxitem_data[name]['maxitemmeasurements']={}

            for maxitemmeasurement in record.maxitemmeasurements.all():

                if maxitemmeasurement.max_item.max_item_name not in maxitem_data[name]['maxitemmeasurements']:
                    maxitem_data[name]['maxitemmeasurements'][maxitemmeasurement.max_item.max_item_name] = []
                maxitem_data[name]['maxitemmeasurements'][maxitemmeasurement.max_item.max_item_name].append(
                    {'created': maxitemmeasurement.created, 'weight': maxitemmeasurement.weight}
                )
        return JsonResponse(maxitem_data)

    # return HttpResponse(status=400, reason='Only GET requests are allowed')


class MaxTableView(LoginRequiredMixin, ListView):

    model = MaxMultipleMeasurement
    template_name = 'tracking/max_table.html'
 
    def get_queryset(self):
        return MaxMultipleMeasurement.objects.filter(
            max_record=MaxMultipleRecord.objects.get(max_user=self.request.user))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page'] = 'max_table'
        

        measurements = []

        for measurement in data['object_list']:
            measurements.append({
                'max_item': measurement.max_item,
                'created': measurement.created if measurement.created != date.today() else 'Today',
                'weight': measurement.weight,
                'unit':measurement.unit,
            })

        data['object_list'] = measurements

        return data

class AddMaxMultipleView(LoginRequiredMixin, CreateView):
    fields = ['max_item','weight','unit','created']
    template_name = 'tracking/max_form.html'
    success_url = reverse_lazy('tracking:tracking')

    model = MaxMultipleMeasurement

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page'] = 'max_form'
        data['show_form'] = True

        latest = MaxMultipleMeasurement.objects.filter(
            max_record=MaxMultipleRecord.objects.get(max_user=self.request.user)
        )

        if latest and latest[0].created == date.today():
            data['show_form'] = False

        return data

    def form_valid(self, form):
        form.instance.max_record = MaxMultipleRecord.objects.get(max_user=self.request.user)
        return super().form_valid(form)