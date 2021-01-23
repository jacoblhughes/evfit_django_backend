from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework import permissions

class EFHabitViewset(viewsets.ModelViewSet):
    serializer_class = serializers.EFHabitSerializer

    def get_queryset(self, *args, **kwargs):
        return models.Habit.objects.all().order_by('id')

    permission_classes = (permissions.IsAuthenticated,)
