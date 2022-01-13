from rest_framework import serializers

from zone.models import Zone


class ZoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['zone_type', 'lat', 'lon', 'radius', 'description', 'is_showing']


class ToShowZoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['zone_type', 'lat', 'lon', 'radius', 'description']