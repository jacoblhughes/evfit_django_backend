from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework import permissions
from rest_framework import authentication

class ProfileViewset(viewsets.ModelViewSet):

    def get_queryset(self, *args, **kwargs):
        return models.Profile.objects.filter(user=self.request.user)
    # queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    