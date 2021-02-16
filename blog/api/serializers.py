from rest_framework import serializers
from .. import models

class EFBlogSerializer(serializers.ModelSerializer):

    authorname = serializers.CharField(source='author.username', read_only=True)


    class Meta:
        model = models.BlogPost
        fields = ('id','title','content','created_on','authorname')