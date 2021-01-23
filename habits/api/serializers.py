from rest_framework import serializers
from .. import models

class EFHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Habit
        fields = ('id','name','description')