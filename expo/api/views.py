from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework import permissions


class ExpoRecordViewset(viewsets.ModelViewSet):

    def get_queryset(self, *args, **kwargs):
        # return models.ExpoRecord.objects
        user = self.request.user
        return models.ExpoRecord.objects.filter(expo_user = user)
    # queryset = models.HabitMeasurement.objects.all()
    serializer_class = serializers.ExpoRecordSerializer
    permission_classes = (permissions.IsAuthenticated,)
