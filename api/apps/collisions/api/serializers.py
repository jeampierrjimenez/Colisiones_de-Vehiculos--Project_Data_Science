from rest_framework import serializers
from apps.collisions.models import *


class CollisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MotorVehicleCollisionsCrashes
        fields = ['id_collision', 'crash_date', 'borough', 'latitude', 'longitude', 'on_street_name',
                  'number_of_persons_injured', 'number_of_persons_killed']


class TimeCrashPercSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeCrashPerc
        fields = '__all__'


class ZoneCrashSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZoneCrash
        exclude = ('id_zone_crash', )


class PublicDamageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicDamage
        exclude = ('id_public_damage', )


class LicenceStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = LicenceStates
        exclude = ('id_licence_states', )


class FactorBySexSerializer(serializers.ModelSerializer):

    class Meta:
        model = FactorBySex
        exclude = ('id_factor_by_sex', )


class DataMonthlyByTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataMonthlyByType
        exclude = ('id_data_monthly_by_type', )


class DataMonthlyByStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataMonthlyByStatus
        exclude = ('id_data_monthly_by_status', )


class DataMonthlyBySexSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataMonthlyBySex
        exclude = ('id_monthly_by_sex', )


class DataMonthlyByInjurySerializer(serializers.ModelSerializer):

    class Meta:
        model = DataMonthlyByInjury
        exclude = ('id_monthly_by_injury', )
