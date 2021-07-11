from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework import permissions


class WorkoutTemplateViewset(viewsets.ModelViewSet):

    def get_queryset(self, *args, **kwargs):
        # return models.ExpoRecord.objects
        return models.WorkoutTemplate.objects.all()
    # queryset = models.HabitMeasurement.objects.all()
    serializer_class = serializers.WorkoutTemplateSerializer
    # permission_classes = (permissions.IsAuthenticated,)
