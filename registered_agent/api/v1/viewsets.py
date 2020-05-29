from rest_framework import authentication
from registered_agent.models import Registered_agent
from .serializers import Registered_agentSerializer
from rest_framework import viewsets


class Registered_agentViewSet(viewsets.ModelViewSet):
    serializer_class = Registered_agentSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Registered_agent.objects.all()
