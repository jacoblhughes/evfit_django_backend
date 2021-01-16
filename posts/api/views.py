from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework import permissions
from rest_framework import authentication

class EFPostViewset(viewsets.ModelViewSet):

    queryset = models.Post.objects.all().order_by('-created_on')
    serializer_class = serializers.EFPostSerializer
    permission_classes = (permissions.IsAuthenticated,)
