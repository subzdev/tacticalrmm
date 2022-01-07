from rest_framework import serializers
from .models import Integration


class GetIntegrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        fields = ('id', 'name', 'description', 'configuration', 'enabled')

class GetIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        fields = ('id', 'name', 'description', 'configuration', 'enabled')