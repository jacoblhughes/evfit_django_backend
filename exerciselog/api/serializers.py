from rest_framework import serializers
from .. import models

class ExerciseInformationSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.ExerciseInformation
        fields = ('id','exerciseRecord','exercise')