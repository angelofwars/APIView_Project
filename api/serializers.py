from rest_framework import serializers
from .models import DRF_Test

class DRF_TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRF_Test
        fields = ('id',
                  'name',
                  'roll',
                  'city',)