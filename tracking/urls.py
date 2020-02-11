from django.urls import path

import tracking.views

app_name = 'tracking'

urlpatterns = [
    path('', tracking.views.TrackingHome.as_view(), name='tracking'),
    path('weight_data/', tracking.views.WeightData.as_view(), name='weight_data'),
    path('weight_table/', tracking.views.WeightTableView.as_view(), name='weight_table'),
    path('rmbacksquat_data/', tracking.views.RMBackSquatData.as_view(), name='rmbacksquat_data'),
    path('rmbacksquat_table/', tracking.views.RMBackSquatTableView.as_view(), name='rmbacksquat_table'),
    path('habit_data/', tracking.views.HabitData.as_view(), name='habit_data'),
    path('habit_table/', tracking.views.HabitTableView.as_view(), name='habit_table'),
    path('add/', tracking.views.AddWeightMeasurementView.as_view(), name='add'),
]
