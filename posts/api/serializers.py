from rest_framework import serializers
from .. import models

class EFPostSerializer(serializers.ModelSerializer):
    # habit_name = serializers.SerializerMethodField()

    # def get_habit(self, obj):
    #     return obj.habit_name.name
    habit_name = serializers.CharField(source='habit.name')
    username = serializers.CharField(source='user.username')


    class Meta:
        model = models.Post
        fields = ('user','created_at','message','message_html','habit','habit_name','username')