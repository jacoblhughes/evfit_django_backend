from rest_framework import serializers
from .. import models

class ExpoRecordSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.ExpoRecord
        fields = ('id','expo_user','expoToken','expoAccepted')