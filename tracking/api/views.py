from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework import permissions


class EFHabitMeasViewset(viewsets.ModelViewSet):

    def get_queryset(self, *args, **kwargs):
        return models.HabitMeasurement.objects.filter(habit_record=self.request.user.id).order_by('-created')
    # queryset = models.HabitMeasurement.objects.all()
    serializer_class = serializers.EFHabitMeasSerializer
    permission_classes = (permissions.IsAuthenticated,)
