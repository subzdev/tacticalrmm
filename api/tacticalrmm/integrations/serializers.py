from rest_framework import serializers
from .models import Integration


class GetIntegrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
<<<<<<< HEAD
        fields = ('id', 'name', 'description', 'configuration', 'enabled')
=======
        fields = ('id', 'name', 'description', 'configuration', 'enabled', 'client_org_related')
>>>>>>> 5a541b0209a0de11b20c5d153af1efa9333fd4ab

class GetIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
<<<<<<< HEAD
        fields = ('id', 'name', 'description', 'configuration', 'enabled')
=======
        fields = ('id', 'name', 'description', 'configuration', 'enabled', 'client_org_related')
>>>>>>> 5a541b0209a0de11b20c5d153af1efa9333fd4ab