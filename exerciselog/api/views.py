from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework import permissions


class ExerciseRecordViewset(viewsets.ModelViewSet):

    def get_queryset(self, *args, **kwargs):
        # return models.ExpoRecord.objects
        user = self.request.user
        return models.ExerciseRecord.objects.filter(exercise_user = user)
    # queryset = models.HabitMeasurement.objects.all()
    serializer_class = serializers.ExerciseRecordSerializer
    # permission_classes = (permissions.IsAuthenticated,)
