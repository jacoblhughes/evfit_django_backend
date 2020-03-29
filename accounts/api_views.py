from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import permissions

class EFUsersViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all().order_by('-id')
    serializer_class = serializers.EFUserSerializer
    # permission_classes = [permissions.IsAuthenticated]