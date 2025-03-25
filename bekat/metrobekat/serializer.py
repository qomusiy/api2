from rest_framework import serializers
from .models import MetroBekat

class MetroBekatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetroBekat
        fields = '__all__'