from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework import permissions


class EFBlogViewset(viewsets.ModelViewSet):

    queryset = models.BlogPost.objects.filter(status=1).order_by('-created_on')[:5]
    serializer_class = serializers.EFBlogSerializer
    permission_classes = (permissions.IsAuthenticated,)
