from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import (ClientSerializer,
                          CustomerSerializer,
                          ZoneSerializer,
                          SiteSerializer)

from estate.models import Zone, Site
from partners.models import Client, Customer
from rest_framework.views import APIView


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
    API endpoint that allows zones to be viewed or edited.
    """
    queryset = Zone.objects.all().order_by('name')
    serializer_class = ZoneSerializer


class SiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sites to be viewed or edited.
    """
    queryset = Site.objects.all().order_by('name')
    serializer_class = SiteSerializer


class SiteByZoneList(APIView):
    """
    Retrieve, site instances by zone.
    """

    def get(self, request, zone_id, format=None):
        sites = Site.objects.filter(zone_id=zone_id)
        serializers = [SiteSerializer(site, context={'request': request}) for site in sites]
        return Response([serializer.data for serializer in serializers])
