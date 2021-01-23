from rest_framework import serializers
from .. import models

class EFHabitMeasSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.HabitMeasurement
        fields = ('id','habit_record','habit','reply','created')