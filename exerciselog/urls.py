from django.urls import path

import exerciselog.views

app_name = 'exerciselog'

urlpatterns = [
    # path('weight_add', tracking.views.AddWeightView.as_view(), name='weight_add'),
    # path('weight_data/', tracking.views.WeightData.as_view(), name='weight_data'),
    # path('weight_table/', tracking.views.WeightTableView.as_view(), name='weight_table'),\
    path('exercise_add', exerciselog.views.CreateExercise.as_view(), name='exercise_add'),
    # path('habit_data/', tracking.views.HabitData.as_view(), name='habit_data'),
    path('exercise_list', exerciselog.views.ListExercise.as_view(), name='exercise_list'),
    # path('max_add', tracking.views.AddMaxMultipleView.as_view(), name='max_add'),
    # path('max_data/', tracking.views.MaxData.as_view(), name='max_data'),
    # path('max_table/', tracking.views.MaxTableView.as_view(), name='max_table'),
]