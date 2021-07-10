from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework import permissions

class EFPostViewset(viewsets.ModelViewSet):
    serializer_class = serializers.EFPostSerializer

    def get_queryset(self, *args, **kwargs):
        return models.HabitPost.objects.all().order_by('created_at')

    permission_classes = (permissions.IsAuthenticated,)
