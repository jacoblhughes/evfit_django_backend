from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework import permissions


class ExerciseInformationViewset(viewsets.ModelViewSet):

    def get_queryset(self, *args, **kwargs):
        return models.ExerciseInformation.objects.filter(exercise_record=self.request.user.id)
    # def get_queryset(self, *args, **kwargs):
    #     user = self.request.user
    #     return models.ExerciseInformation.objects.all()

    serializer_class = serializers.ExerciseInformationSerializer

    permission_classes = (permissions.IsAuthenticated,)