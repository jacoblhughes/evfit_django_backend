from rest_framework import serializers
from . import models

class EFUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EFUser
        fields = ('id','first_name','last_name')
