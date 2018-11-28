from django.contrib.auth.models import User, Group
from rest_framework import serializers

from partners.models import Client, Customer
from estate.models import Zone, Site


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('url', 'name', 'address',)


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('url', 'name', 'address',)


class ZoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zone
        fields = ('url', 'name',)


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('url', 'name',)

