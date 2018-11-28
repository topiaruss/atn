from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import (ClientSerializer,
                          CustomerSerializer,
                          ZoneSerializer,
                          SiteSerializer)

from estate.models import Zone, Site
from partners.models import Client, Customer


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Zone.objects.all().order_by('name')
    serializer_class = ZoneSerializer


class SiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Site.objects.all().order_by('name')
    serializer_class = CustomerSerializer
