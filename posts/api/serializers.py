from rest_framework import serializers
from .. import models

class EFPostSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Post
        fields = ('user','created_at','message','message_html','habit')