from rest_framework import serializers
from apps.traffic.models import *


class TrafficOneSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrafficVolume
        exclude = ('id_traffic',)


class TrafficAltSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrafficVolumeAlt
        exclude = ('id_traffic_volume_alt',)


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CalleBarrioLe
        exclude = ('id_calle_barrio_le',)

