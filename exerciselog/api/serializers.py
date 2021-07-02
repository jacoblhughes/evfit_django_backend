from rest_framework import serializers
from .. import models

class ExerciseRecordSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.ExpoRecord
        fields = ('id','exerciseRecord','exercise')