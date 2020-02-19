from django.urls import path

import tracking.views

app_name = 'tracking'

urlpatterns = [
    path('', tracking.views.TrackingHome.as_view(), name='tracking'),
    path('weight_add', tracking.views.AddWeightView.as_view(), name='weight_add'),
    path('weight_data/', tracking.views.WeightData.as_view(), name='weight_data'),
    path('weight_table/', tracking.views.WeightTableView.as_view(), name='weight_table'),\
    path('habit_add', tracking.views.AddHabitView.as_view(), name='habit_add'),
    path('habit_data/', tracking.views.HabitData.as_view(), name='habit_data'),
    path('habit_table/', tracking.views.HabitTableView.as_view(), name='habit_table'),
    path('max_add', tracking.views.AddMaxMultipleView.as_view(), name='max_add'),
    path('max_data/', tracking.views.MaxData.as_view(), name='max_data'),
    path('max_table/', tracking.views.MaxTableView.as_view(), name='max_table'),
]
