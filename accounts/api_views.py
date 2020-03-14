from rest_framework import viewsets
from . import models
from . import serializers

class EFUserViewset(viewsets.ModelViewSet):
    queryset = models.EFUser.objects.all()
    serializer_class = serializers.EFUserSerializer