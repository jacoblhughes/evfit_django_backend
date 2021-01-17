from rest_framework import serializers
from .. import models

class EFHabitMeasSerializer(serializers.ModelSerializer):
    # habit_record=serializers.SerializerMethodField()
    # habit_name = serializers.SerializerMethodField()

    # def get_habit_record(self, obj):
    #     return obj.habit_record.habit_user.username

    # def get_habit(self, obj):
    #     return obj.habit_name.name

    # habit_record_key = serializers.PrimaryKeyRelatedField(source='habit_record', read_only=True)
    # habit_key = serializers.PrimaryKeyRelatedField(source='habit', read_only=True)



    # habit_record_id = serializers.PrimaryKeyRelatedField(
    #     source='habit_record',
    #     queryset=Animal.objects.all(),
    #     write_only=True
    # )

    # habit = serializers.SerializerMethodField()
    # habit_key = serializers.PrimaryKeyRelatedField(read_only=True)
   
    # habit = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:

        model = models.HabitMeasurement
        fields = ('id','habit_record','habit','reply','created')