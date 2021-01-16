from rest_framework import serializers
from .. import models

class EFBlogSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.BlogPost
        fields = ('id','title','content','created_on')