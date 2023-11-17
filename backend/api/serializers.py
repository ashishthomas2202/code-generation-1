from rest_framework import serializers
from .models import ai

class aiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ai
        fields = ('id', 'name', 'description')