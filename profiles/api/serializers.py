from rest_framework import serializers
from .. import models

class ProfileSerializer(serializers.ModelSerializer):
    habit = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_habit(self, obj):
        return obj.habit.name
    def get_user(self, obj):
        return obj.user.username

    habit_key = serializers.PrimaryKeyRelatedField(source='habit', read_only=True)
    user_key = serializers.PrimaryKeyRelatedField(source='user', read_only=True)



    class Meta:
        model = models.Profile
        fields = ('user','user_key','habit','habit_key')
