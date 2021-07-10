from rest_framework import serializers
from .. import models

class EFHabitMeasSerializer(serializers.ModelSerializer):

    habit_name = serializers.StringRelatedField(source='habit', read_only=True)

    class Meta:

        model = models.HabitMeasurement
        fields = ('id','habit_record', 'habit_name','habit','reply','created')