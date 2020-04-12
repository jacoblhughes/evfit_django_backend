from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework import permissions


class EFBlogViewset(viewsets.ModelViewSet):

    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.EFBlogSerializer
