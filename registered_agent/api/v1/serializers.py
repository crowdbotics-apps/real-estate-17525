from rest_framework import serializers
from registered_agent.models import Registered_agent


class Registered_agentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registered_agent
        fields = "__all__"
