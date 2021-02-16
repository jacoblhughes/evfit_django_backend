from rest_framework import serializers
from .. import models

class EFPostSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = models.HabitPost
        fields = ('user','created_at','message','message_html','habit','username','id')