from rest_framework import serializers
from .. import models

class WorkoutTemplateSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.WorkoutTemplate
        fields = ('category','title','tempalate','notes')